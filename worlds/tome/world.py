from collections.abc import Mapping
from typing import Any

from BaseClasses import Tutorial
from worlds.AutoWorld import World, WebWorld


from . import items, locations, regions, rules
from . import options as tome_options

SLOT_DATA_OPTIONS = ("merge_generic_enemy_locations", "require_all_zones", "objective")


class TOMEWeb(WebWorld):
    game = "Tales of Maj'Eyal"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up TOME for Archipelago.",
        "English",
        "tome_en.md",
        "setup/en",
        ["Mabel"]
    )]


class TOMEWorld(World):
    """
    Tales of Maj'Eyal is an open-source roguelike set in a completely original world.
    """

    game = "Tales of Maj'Eyal"

    options_dataclass = tome_options.TOMEOptions
    options: tome_options.TOMEOptions

    location_name_to_id = locations.ALL_LOCATION_IDS
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Maj'Eyal"

    item_name_groups = items.ITEM_GROUPS

    web = TOMEWeb()

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.TOMEItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            *SLOT_DATA_OPTIONS
        )
