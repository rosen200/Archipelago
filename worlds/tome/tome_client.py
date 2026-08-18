"""Archipelago client for Tales Of Maj'Eyal."""
import asyncio
import socket
import sys
from argparse import Namespace
from enum import Enum
from typing import TYPE_CHECKING, Any, TextIO

from CommonClient import ClientCommandProcessor, CommonContext, logger, server_loop, gui_enabled, get_base_parser
from NetUtils import ClientStatus

from .locations import ALL_LOCATION_IDS, ENEMY_LOCATIONS, get_location_name_for_enemy
from .world import SLOT_DATA_OPTIONS


if TYPE_CHECKING:
    import kvui


class ConnectionStatus(Enum):
    NOT_CONNECTED = 0
    SCOUTS_NOT_SENT = 1
    SCOUTS_SENT = 2
    GAME_RUNNING = 3


class TOMEClientCommandProcessor(ClientCommandProcessor):
    ctx: "TOMEContext"


class TOMEContext(CommonContext):
    game = "Tales of Maj'Eyal"
    items_handling = 0b111  # full remote

    last_connected_slot: int | None = None

    slot_data: dict[str, Any]

    connection_status: ConnectionStatus = ConnectionStatus.NOT_CONNECTED

    highest_processed_item_index: int = 0
    queued_locations: list[int]

    command_processor = TOMEClientCommandProcessor

    def __init__(
        self, server_address: str | None = None, password: str | None = None
    ) -> None:
        super().__init__(server_address, password)

        self.queued_locations = []
        self.slot_data = {}

    async def server_auth(self, password_requested: bool = False) -> None:
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect(game=self.game)

    def on_package(self, cmd: str, args: dict[str, Any]) -> None:
        if cmd == "Connected":
            for option in SLOT_DATA_OPTIONS:
                if option not in args["slot_data"]:
                    raise KeyError(
                        f"Missing slot data key {option},"
                        " was this game generated on an older version?")

            self.slot_data = args["slot_data"]

        if cmd == "RoomInfo":
            self.seed_name = args["seed_name"]

    async def disconnect(self, *args: Any, **kwargs: Any) -> None:
        self.connection_status = ConnectionStatus.NOT_CONNECTED
        await super().disconnect(*args, **kwargs)

    def make_gui(self):
        ui = super().make_gui()
        ui.base_title = "Archipelago TOME Client"
        ui.logging_pairs = [("Client", "Archipelago")]

        return ui


LOCATION_PREFIX = "APLOCATION"
SEND_ITEMS_PREFIX = "APSENDITEMS"

class TOMEAddonConnection():
    server_socket: socket.socket | None = None
    connection: socket.socket | None = None
    connection_file: TextIO | None = None

    def __init__(self, ctx):
        self.ctx = ctx
        self.locations_checked = set(self.ctx.locations_checked)

    def strip_gloom_prefix(self, name):
        gloom_prefixes = ["gloomy ", "deformed ", "sick ", "dreaming ", "slumbering ", "dozing "]
        for prefix in gloom_prefixes:
            prefix_len = len(prefix)
            if name.startswith(prefix) and name[prefix_len:] in ALL_LOCATION_IDS:
                return name[prefix_len:]
        return name

    def tier1_victory(self):
        bosses = ["Prox the Mighty", "Shax the Slimy",
                  "Spellblaze Crystal", "Norgos, the Guardian",
                  "Norgos, the Frozen", "The Shade", "The Possessed",
                  "Rhaloren Inquisitor", "The Withering Thing",
                  "The Dreaming One"]
        return all(self.get_id_for_location(boss) in self.locations_checked for boss in bosses)

    def tier2_victory(self):
        bosses = ["Shardskin", "Wrathroot", "Sandworm Queen",
                  "Horned Horror", "Minotaur of the Labyrinth",
                  "Rantha the Worm", "Varsha the Writhing"]
        return all(self.get_id_for_location(boss) in self.locations_checked for boss in bosses)

    def dreadfell_victory(self):
        return self.get_id_for_location("The Master") in self.locations_checked

    def tannen_victory(self):
        bosses = ["Tannen", "Drolem"]
        return all(self.get_id_for_location(boss) in self.locations_checked for boss in bosses)

    def sorcerors_victory(self):
        bosses = ["Elandar", "Argoniel"]
        return all(self.get_id_for_location(boss) in self.locations_checked for boss in bosses)


    def has_victory(self):
        if self.ctx.slot_data["objective"] == 0:
            return self.tier1_victory()
        if self.ctx.slot_data["objective"] == 1:
            return self.tier2_victory()
        if self.ctx.slot_data["objective"] == 2:
            return self.dreadfell_victory()
        if self.ctx.slot_data["objective"] == 3:
            return self.tannen_victory()
        if self.ctx.slot_data["objective"] == 4:
            return self.sorcerors_victory()
        return False

    def get_id_for_location(self, name):
        if name not in ENEMY_LOCATIONS:
            return None
        data = ENEMY_LOCATIONS[name]
        location_name = get_location_name_for_enemy(
            data, not self.ctx.slot_data["require_all_zones"],
            self.ctx.slot_data["merge_generic_enemy_locations"])
        if location_name not in ALL_LOCATION_IDS:
            logger.error("Couldn't find id for %s!", location_name)
            return None
        return ALL_LOCATION_IDS[location_name]

    def handle_location_exceptions(self, location):
        if (location == "Kroltar the Scourge" and
            not self.ctx.slot_data["require_all_zones"]):
            # Change this another bonus zone boss to guarantee that
            # any given character can get the boss location even if
            # bonus zone rolls scourge pits. Remove this once DLC is
            # supported.
            return "Mindworm"
        return location

    def handle_location_message(self, message):
        location = message[len(LOCATION_PREFIX):].strip()
        location = self.strip_gloom_prefix(location)
        location = self.handle_location_exceptions(location)
        location_id = self.get_id_for_location(location)
        if not location_id:
            return
        self.locations_checked.add(location_id)
        if self.has_victory():
            asyncio.run(self.ctx.send_msgs([
                {"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}]))
            self.ctx.finished_game = True
        asyncio.run(self.ctx.check_locations(self.locations_checked))

    def handle_message(self, message):
        if not self.connection or not self.connection_file:
            return
        if message.startswith(LOCATION_PREFIX):
            self.handle_location_message(message)
        elif message.startswith(SEND_ITEMS_PREFIX):
            try:
                # Lua stores all numbers as floats, get an integer
                already_sent = int(float(message[len(SEND_ITEMS_PREFIX):].strip()))
            except:
                logger.error('Non-integer item number received from addon')
                return
            to_send = len(self.ctx.items_received) - already_sent
            number_message = f"APNUMITEMS {to_send}\n"
            self.connection_file.write(number_message)
            if to_send > 0:
                for item in self.ctx.items_received[already_sent:]:
                    name = self.ctx.item_names.lookup_in_game(item.item)
                    self.connection_file.write(f"APITEM {name}\n")
            self.connection_file.flush()


    def game_connection(self):
        logger.info('Starting network connection on port 31821')
        self.server_socket = socket.create_server(('localhost', 31821))
        while not self.ctx.exit_event.is_set():
            try:
                if not self.connection or not self.connection_file:
                    try:
                        self.connection, _ = self.server_socket.accept()
                        self.connection_file = self.connection.makefile(mode='rw')
                        logger.info("Connected to addon!")
                    except TimeoutError:
                        continue
                else:
                    try:
                        message = self.connection_file.readline()
                        if not message:
                            logger.info("Connection closed by TOME")
                            self.connection_file.close()
                            self.connection.close()
                            self.connection_file = None
                            self.connection = None
                            continue
                    except TimeoutError:
                        continue
                    except ConnectionResetError:
                        logger.info("Connection reset by TOME")
                        self.connection_file.close()
                        self.connection.close()
                        self.connection_file = None
                        self.connection = None
                        continue
                    self.handle_message(message)
            except Exception as e:
                if not self.ctx.exit_event.is_set():
                    if self.connection_file is not None:
                        logger.error("Encountered an error: %s", e)
                    else:
                        logger.error(
                            "TOME Client cannot process locations while disconnected.")
        # Close socket on exit
        if self.connection:
            self.connection_file.close()
            self.connection.close()

    def shutdown(self):
        if self.connection:
            logger.info('closing connection socket')
            self.connection.shutdown(socket.SHUT_RDWR)
        if self.server_socket:
            logger.info('closing server socket')
            self.server_socket.shutdown(socket.SHUT_RDWR)


def launch_tome_client():
    async def main(args: Namespace) -> None:
        logger.info('Starting TOME Client...')
        ctx = TOMEContext(args.connect, args.password)
        if hasattr(args, 'name'):
            ctx.auth = args.name
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")

        if gui_enabled:
            ctx.run_gui()

            connection = TOMEAddonConnection(ctx)
            connection_runner = asyncio.create_task(asyncio.to_thread(
                connection.game_connection))

            await ctx.exit_event.wait()
            ctx.server_address = None
            logger.info('Waiting for TOME addon connection to close...')
            connection.shutdown()
            await connection_runner
            await ctx.shutdown()

    import colorama
    parser = get_base_parser(description="TOME Client, for text interfacing.")
    args, _ = parser.parse_known_args()
    colorama.init()
    asyncio.run(main(args))
    colorama.deinit()


if __name__ == "__main__":
    launch_tome_client(*sys.argv[1:])
