from __future__ import annotations
import dataclasses

from typing import TYPE_CHECKING

from BaseClasses import Region
from rule_builder.rules import Has, HasGroupUnique, Rule, True_

if TYPE_CHECKING:
    from .world import TOMEWorld


@dataclasses.dataclass
class TOMEZone:
    name: str
    enemies: list[str]
    variants: dict[str, list[str]]
    tier: str
    entrance_rule: Rule
    has_backup_guardian: bool = False
    required_start: str = ''

ZONES = [
    TOMEZone(
        name="Trollmire",
        enemies=["Trolls Tier 1", "Vermin Tier 1", "Snake Tier 1",
                 "Plant Tier 1", "Swarm Tier 1", "Bear Tier 1"],
        variants={"normal": ["Canines Tier 1"], "flooded": ["Aquatic Critter Tier 1"]},
        tier="Tier 1",
        entrance_rule=Has("Trollmire"),
        has_backup_guardian=True,
    ),
    TOMEZone(
        name="Scintillating Caves",
        enemies=["Crystal Tier 1", "Vermin Tier 1", "Snake Tier 1", "Bear Tier 1", "Rodent Tier 1"],
        variants={},
        tier="Tier 1",
        entrance_rule=Has("Scintillating Caves"),
        has_backup_guardian=True,
    ),
    TOMEZone(
        name="Norgos' Lair",
        enemies=["Canines Tier 1", "Vermin Tier 1", "Snake Tier 1", "Bear Tier 1"],
        variants={"normal": [], "invaded": ["Shivgoroth Tier 1"]},
        tier="Tier 1",
        entrance_rule=Has("Norgos' Lair"),
    ),
    TOMEZone(
        name="Kor'Pul",
        enemies=["Rodent Tier 1", "Vermin Tier 1", "Snake Tier 1", "Molds Tier 1"],
        variants={"normal": ["Skeletons Tier 1"], "hideout": ["Thieves Tier 1"]},
        tier="Tier 1.5",
        entrance_rule=Has("Kor'Pul"),
        has_backup_guardian=True,
    ),
    TOMEZone(
        name="Heart of the Gloom",
        enemies=["Rodent Tier 1", "Vermin Tier 1", "Snake Tier 1", "Plant Tier 1"],
        variants={},
        tier="Tier 1.5",
        entrance_rule=Has("Heart of the Gloom")
    ),
    TOMEZone(
        name="Rhaloren Camp",
        enemies=["Elven Warriors Tier 1", "Elven Casters Tier 1",
                 "Rodent Tier 1", "Vermin Tier 1", "Molds Tier 1"],
        variants={},
        tier="Tier 1.5",
        entrance_rule=Has("Rhaloren Camp")
    ),
    TOMEZone(
        name="Southeast Derth",
        enemies=[],
        # Missable zone
        variants={"missable": ["Gladiator Tier 1"]},
        tier="Tier 1",
        entrance_rule=True_(),
    ),
    TOMEZone(
        name="Old Forest",
        enemies=["Bear Tier 1", "Bear Tier 2", "Ant Tier 1", "Ant Tier 2",
                 "Plant Tier 1", "Plant Tier 2", "Snake Tier 1",
                 "Swarm Tier 1", "Vermin Tier 1"],
        variants={"normal": ["Canines Tier 1"], "crystalized": ["Crystal Tier 1"]},
        tier="Tier 2",
        entrance_rule=Has("Old Forest"),
        has_backup_guardian=True,
    ),
    TOMEZone(
        name="Sandworm Lair",
        enemies=["Sandworm Tier 1", "Vermin Tier 1", "Ooze Tier 1", "Ooze Tier 2", "Jelly Tier 1"],
        variants={},
        tier="Tier 2",
        entrance_rule=Has("Sandworm Lair"),
        has_backup_guardian=True,
    ),
    TOMEZone(
        name="Maze",
        enemies=["Jelly Tier 1", "Ooze Tier 1", "Ooze Tier 2",
                 "Thieves Tier 1", "Thieves Tier 2", "Canines Tier 1"],
        variants={"normal": ["Minotaur Tier 2", "Ant Tier 1",
                             "Ant Tier 2", "Vermin Tier 1", "Rodent Tier 1"],
                  "collapsed": ["Corrupted Horror Tier 1",
                                "Temporal Horror Tier 2"]
                  },
        tier="Tier 2",
        entrance_rule=Has("Maze"),
        has_backup_guardian=True,
    ),
    TOMEZone(
        name="Daikara",
        enemies=["Xorn Tier 2", "Snow Giant Tier 2"],
        variants={"normal": ["Cold Drake Tier 2", "Canines Tier 1"],
                  # Faeros can spawn but are too rare to be reliable.
                  "erupting": ["Fire Drake Tier 2"]},
        tier="Tier 2",
        entrance_rule=Has("Daikara"),
        has_backup_guardian=True,
    ),
    TOMEZone(
        name="Stormed Derth",
        enemies=["Gwelgoroth Tier 2"],
        variants={},
        tier="Tier 2",
        entrance_rule=HasGroupUnique("Tier 2 Zones", count=2)
    ),
    TOMEZone(
        name="Lumberjack Village",
        # Just a boss
        enemies=[],
        variants={},
        tier="Tier 2",
        entrance_rule=True_()
    ),
    TOMEZone(
        name="Ruined Dungeon",
        # Almost any enemy in the game can spawn here.
        # No single enemy is likely enough to be here to consider in logic.
        enemies=[],
        variants={},
        tier="Misc Pre-Dreadfell",
        entrance_rule=Has("Ruined Dungeon")
    ),
    TOMEZone(
        name="Halfling Ruins",
        enemies=["Skeletons Tier 1", "Skeletons Tier 2", "Ghoul Tier 1", "Ghoul Tier 2"],
        variants={},
        tier="Misc Pre-Dreadfell",
        entrance_rule=Has("Halfling Ruins")
    ),
    TOMEZone(
        name="Ring of Blood",
        enemies=["Slave Tier 2"],
        variants={},
        tier="Misc Pre-Dreadfell",
        entrance_rule=Has("Ring of Blood")
    ),
    TOMEZone(
        name="Golem Graveyard",
        enemies=["Golem Tier 1", "Golem Tier 2",],
        variants={},
        tier="Misc Pre-Dreadfell",
        entrance_rule=Has("Golem Graveyard")
    ),
    TOMEZone(
        name="Lake of Nur",
        enemies=["Aquatic Critter Tier 1", "Aquatic Critter Tier 2",
                 "Aquatic Demon Tier 2"],
        variants={"normal": ["Snake Tier 1", "Plant Tier 1", "Plant Tier 2",
                             "Horror Tier 3", "Horror Tier 2"],
                         "flooded": ["Aquatic Horror Tier 2"]},
        tier="Misc Pre-Dreadfell",
        entrance_rule=Has("Old Forest")
    ),
    TOMEZone(
        name="Mark of the Spellblaze",
        enemies=["Elven Casters Tier 1", "Elven Casters Tier 3",
                 "Faeros Tier 3", "Gwelgoroth Tier 2", "Rodent Tier 1", "Vermin Tier 1"],
        variants={},
        tier="Misc Pre-Dreadfell",
        entrance_rule=Has("Mark of the Spellblaze")
    ),
    TOMEZone(
        name="Tempest Peak",
        enemies=["Gwelgoroth Tier 2", "Xorn Tier 2", "Snow Giant Tier 2",
                 "Storm Drake Tier 2"],
        variants={},
        tier="Misc Pre-Dreadfell",
        entrance_rule=HasGroupUnique("Pre-Dreadfell Zones", count=1),
    ),
    TOMEZone(
        name="Temporal Rift",
        enemies=["Temporal Horror Tier 2", "Temporal Horror Tier 3",
                 "Telugoroth Tier 2", "Telugoroth Tier 3"],
        variants={},
        tier="Misc Pre-Dreadfell",
        entrance_rule=Has("Daikara"),
    ),
    TOMEZone(
        name="Last Hope Graveyard",
        # Only bosses
        enemies=[],
        variants={},
        tier="Misc Pre-Dreadfell",
        entrance_rule=HasGroupUnique("Pre-Dreadfell Zones", count=1),
    ),
    TOMEZone(
        name="Unknown Tunnels",
        enemies=[],
        # Missable zone
        variants={"missable": ["Thieves Tier 1"]},
        tier="Misc Pre-Dreadfell",
        entrance_rule=True_(),
        has_backup_guardian=True,
    ),

    TOMEZone(
        name="Dreadfell",
        enemies=["Skeletons Tier 1", "Skeletons Tier 2", "Ghoul Tier 1",
                 "Ghoul Tier 2", "Vampire Tier 2", "Vampire Tier 3",
                 "Wight Tier 2", "Wight Tier 3", "Ghost Tier 3"],
        variants={},
        tier="Misc Pre-Dreadfell",
        entrance_rule=(Has("Dreadfell") &
                       HasGroupUnique("Tier 2 Zones", count=4) &
                       HasGroupUnique("Pre-Dreadfell Zones", count=1)),
        has_backup_guardian=True,
    ),
    TOMEZone(
        name="Reknor",
        enemies=["Trolls Tier 1", "Trolls Tier 2", "Trolls Tier 3", "Orc Tier 1", "Orc Tier 2"],
        variants={},
        tier="Early East/West",
        entrance_rule=Has("Reknor"),
        has_backup_guardian=True,
    ),
    TOMEZone(
        name="Briagh's Lair",
        enemies=["Sandworm Tier 1", "Sandworm Tier 3"],
        variants={},
        tier="Early East/West",
        entrance_rule=Has("Reknor")
    ),
    TOMEZone(
        name="Vor Armoury",
        enemies=["Orc Tier 1", "Orc Tier 2", "Vor Orc Tier 4",
                 "Bone Giant Tier 3", "Bone Giant Tier 4",
                 "Grushnak Orc Tier 4"],
        variants={},
        tier="Early East/West",
        entrance_rule=Has("Reknor")
    ),
    TOMEZone(
        name="Unremarkable Cave",
        enemies=["Rodent Tier 1", "Vermin Tier 1", "Molds Tier 1",
                 "Snake Tier 1", "Skeletons Tier 1", "Skeletons Tier 2"],
        variants={},
        tier="Early East/West",
        entrance_rule=Has("Reknor")
    ),
    TOMEZone(
        name="Ardhungol",
        enemies=["Spider Tier 1", "Spider Tier 2", "Spider Tier 4"],
        variants={},
        tier="Early East/West",
        entrance_rule=Has("Reknor") & Has("Ardhungol")
    ),
    TOMEZone(
        name="Bonus Zone",
        enemies=[],
        # This is actually three zones (four with the cults DLC), but
        # can be treated as alt versions for logic. This does
        # sacrifice the ability to include sludgenest/caldera without
        # Halfling ruins but that's probably not worth the added
        # complexity.
        variants={
            "sludgenest": ["Jelly Tier 1", "Ooze Tier 1", "Ooze Tier 2",
                           "Ooze Tier 3"],
            "conclave vault": ["Ogre Tier 3", "Conclave Ogre Tier 3"],
            "dogroth caldera": ["Bear Tier 1", "Bear Tier 2", "Vermin Tier 1",
                                "Canines Tier 1", "Canines Tier 2",
                                "Plant Tier 1", "Plant Tier 2",
                                "Venom Drake Tier 2",
                                "Venom Drake Tier 3", "Faeros Tier 2",
                                "Faeros Tier 3"]
        },
        tier="Early East/West",
        # This could be conclave vault, which requires Halfling Ruins
        entrance_rule=Has("Bonus Zone") & Has("Halfling Ruins")
    ),
    TOMEZone(
        name="Crypt of Kryl'Feijan",
        enemies=[],
        # Missable zone
        variants={"missable": ["Elven Warriors Tier 1", "Elven Casters Tier 1",
                         "Minor Demon Tier 2", "Minor Demon Tier 3",
                         "Elven Warriors Tier 2", "Elven Casters Tier 3"]},
        tier="Early East/West",
        entrance_rule=Has("Reknor"),
        has_backup_guardian=True,
    ),
    TOMEZone(
        name="Tannen's Quest",
        enemies=[],
        # These are technically two mutually exclusive zones, but for
        # logic purposes they work well being treated as an alt
        # versions with no overlap.
        variants={"telmur": ["Skeletons Tier 1", "Skeletons Tier 2",
                         "Ghoul Tier 1", "Ghoul Tier 2",
                         "Bone Giant Tier 3", "Bone Giant Tier 4"],
                         "fearscape": ["Minor Demon Tier 2", "Minor Demon Tier 3",
                         "Major Demon Tier 4"]},
        tier="Early East/West",
        entrance_rule=Has("Reknor") & Has("Tannen")
    ),
    TOMEZone(
        name="Tannen's Tower",
        enemies=["Aquatic Critter Tier 1", "Aquatic Critter Tier 2",
                 "Aquatic Demon Tier 2", "Skeletons Tier 1",
                 "Skeletons Tier 2", "Ghoul Tier 1",
                 "Ghoul Tier 2", "Multihued Drake Tier 2",
                 "Multihued Drake Tier 3", "Multihued Drake Tier 4",
                 "Bone Giant Tier 3", "Bone Giant Tier 4"],
        variants={},
        tier="Early East/West",
        entrance_rule=Has("Reknor") & Has("Tannen")
    ),
    TOMEZone(
        name="Flooded Cave",
        enemies=["Aquatic Critter Tier 1", "Aquatic Critter Tier 2", "Aquatic Demon Tier 2"],
        variants={},
        tier="Early East/West",
        entrance_rule=Has("Reknor") & Has("Flooded Cave")
    ),
    TOMEZone(
        name="Temple of Creation",
        enemies=["Naga Tier 4", "Naga Tier 5"],
        variants={},
        tier="Early East/West",
        entrance_rule=Has("Reknor") & Has("Flooded Cave")
    ),
    TOMEZone(
        name="Shadow Crypt",
        # Every animal, humanoid, and giant can rarely spawn here.
        enemies=[],
        variants={},
        tier="Orc Prides",
        entrance_rule=Has("Shadow Crypt")
    ),
    TOMEZone(
        name="Rak'Shor Pride",
        enemies=["Orc Tier 1", "Orc Tier 2", "Undead Horror Tier 2",
                 "Rak'Shor Orc Tier 3", "Rak'Shor Orc Tier 4",
                 "Bone Giant Tier 3", "Bone Giant Tier 4", "Bone Giant Tier 5"],
        variants={},
        tier="Orc Prides",
        entrance_rule=Has("Rak'Shor Pride")
    ),
    TOMEZone(
        name="Vor Pride",
        enemies=["Orc Tier 1", "Orc Tier 2", "Vor Orc Tier 4"],
        variants={},
        tier="Orc Prides",
        entrance_rule=Has("Vor Pride")
    ),
    TOMEZone(
        name="Gorbat Pride",
        enemies=["Orc Tier 1", "Orc Tier 2", "Gorbat Orc Tier 4",
                 "Cold Drake Tier 2", "Fire Drake Tier 2",
                 "Storm Drake Tier 2", "Venom Drake Tier 2",
                 "Cold Drake Tier 3", "Fire Drake Tier 3",
                 "Storm Drake Tier 3", "Venom Drake Tier 3",
                 "Multihued Drake Tier 2", "Multihued Drake Tier 3",
                 "Wild Drake Tier 4", "Wild Drake Tier 5"],
        variants={},
        tier="Orc Prides",
        entrance_rule=Has("Gorbat Pride")
    ),
    TOMEZone(
        name="Grushnak Pride",
        enemies=["Orc Tier 1", "Orc Tier 2", "Grushnak Orc Tier 4",
                 "Ooze Tier 1", "Ooze Tier 2", "Ooze Tier 3", "Jelly Tier 1"],
        variants={},
        tier="Orc Prides",
        entrance_rule=Has("Grushnak Pride")
    ),
    TOMEZone(
        name="Elven Ruins",
        enemies=["Skeletons Tier 1", "Skeletons Tier 2", "Mummy Tier 1",
                 "Mummy Tier 3"],
        variants={},
        tier="Orc Prides",
        entrance_rule=Has("Elven Ruins")
    ),
    TOMEZone(
        # Also includes the charred scar
        name="Erúan",
        enemies=["Fire Drake Tier 3", "Fire Drake Tier 2", "Faeros Tier 3",
                 "Ritch Tier 3", "Ritch Tier 4"],
        variants={},
        tier="Orc Prides",
        entrance_rule=HasGroupUnique("Pride Zones", count=1)
    ),
    TOMEZone(
        # Caverns leading to this zone have the same enemies.
        name="Valley of the Moon",
        enemies=[],
        # The enemies are common, but the zone itself isn't guaranteed.
        variants={"missable": ["Minor Demon Tier 2", "Minor Demon Tier 3",
                               "Major Demon Tier 4", "Major Demon Tier 5"]},
        tier="Endgame",
        # Handled by Endgame tier
        entrance_rule=True_()
    ),
    TOMEZone(
        name="Slime Tunnels",
        enemies=["Ooze Tier 1", "Ooze Tier 2", "Ooze Tier 3", "Jelly Tier 1"],
        variants={},
        tier="Endgame",
        # Handled by Endgame tier
        entrance_rule=True_()
    ),
    TOMEZone(
        name="High Peak",
        # Nothing is common enough to be in logic here.
        enemies=[],
        variants={},
        tier="Endgame",
        # Handled by Endgame tier
        entrance_rule=True_()
    ),
    TOMEZone(
        name="Escape From Reknor",
        enemies=["Orc Tier 1", "Rodent Tier 1", "Vermin Tier 1", "Snake Tier 1",
                 "Molds Tier 1"],
        variants={},
        tier="Tier 1",
        entrance_rule=True_(),
        required_start="Dwarf",
    ),
    TOMEZone(
        # Not a typo, this is the actual zone name in game
        name="Deep Bellow",
        enemies=["Corrupted Horror Tier 1", "Rodent Tier 1"],
        variants={},
        tier="Tier 1",
        entrance_rule=True_(),
        has_backup_guardian=True,
        required_start="Dwarf",
    ),
    TOMEZone(
        name="Ritch Tunnels",
        enemies=["Ant Tier 1", "Jelly Tier 1", "Vermin Tier 1",
                 "Rel Ritch Tier 1"],
        variants={},
        tier="Tier 1",
        entrance_rule=True_(),
        required_start="Yeek",
    ),
    TOMEZone(
        name="Murgol's Lair",
        enemies=["Aquatic Critter Tier 1", "Aquatic Critter Tier 2",
                 "Yaech Tier 1"],
        variants={"normal": [], "invaded": ["Naga Tier 1"]},
        tier="Tier 1",
        entrance_rule=True_(),
        required_start="Yeek",
    ),
    TOMEZone(
        name="Blighted Ruins",
        # Ghouls can spawn here, but the player is too low level for
        # that to be consistent.
        enemies=["Skeletons Tier 1", "Rodent Tier 1", "Vermin Tier 1",
                 "Blighted Ruins Horror Tier 1"],
        variants={},
        tier="Tier 1",
        entrance_rule=True_(),
        required_start="Undead",
    ),
    TOMEZone(
        name="Abashed Expanse",
        enemies=["Losgoroth Tier 1"],
        variants={},
        tier="Tier 1",
        entrance_rule=True_(),
        required_start="Archmage",
    ),
    TOMEZone(
        name="Slazish Fens",
        enemies=["Naga Tier 1"],
        variants={},
        tier="Tier 1",
        entrance_rule=True_(),
        required_start="Celestial",
    ),
    TOMEZone(
        name="Unhallowed Morass",
        enemies=["Chronomancer Spider Tier 1"],
        variants={},
        tier="Tier 1",
        entrance_rule=True_(),
        required_start="Chronomancer",
    ),
    TOMEZone(
        name="Tranquil Meadow",
        enemies=["Caravaneer Tier 1", "Cursed Shadow Tier 2",
                 "Cursed Canine Tier 2", "Canines Tier 1"],
        variants={},
        tier="Misc Pre-Dreadfell",
        entrance_rule=True_(),
        required_start="Cursed",
    ),
]

def create_and_connect_regions(world: TOMEWorld) -> None:
    created_regions = set()
    # Create and connect the tier containers
    eyal = Region("Maj'Eyal", world.player, world.multiworld)
    tier1 = Region("Tier 1", world.player, world.multiworld)
    tier15 = Region("Tier 1.5", world.player, world.multiworld)
    regions = [eyal, tier1, tier15]
    if world.options.objective >= 1:
        tier2 = Region("Tier 2", world.player, world.multiworld)
        regions.append(tier2)
    if world.options.objective >= 2:
        predreadfell = Region("Misc Pre-Dreadfell", world.player, world.multiworld)
        regions.append(predreadfell)
    if world.options.objective >= 3:
        earlyeast = Region("Early East/West", world.player, world.multiworld)
        regions.append(earlyeast)
    if world.options.objective >= 4:
        prides = Region("Orc Prides", world.player, world.multiworld)
        endgame = Region("Endgame", world.player, world.multiworld)
        regions.append(prides)
        regions.append(endgame)

    world.multiworld.regions += regions

    eyal.connect(tier1, "Eyal to Tier 1")
    tier1.connect(tier15, "Tier 1 to Tier 1.5")
    if world.options.objective >= 1:
        tier15.connect(tier2, "Tier 1.5 to Tier 2", HasGroupUnique("Tier 1.5 Zones", count=1))
    if world.options.objective >= 2:
        tier2.connect(predreadfell, "Tier 2 to Pre-Dreadfell",
                      HasGroupUnique("Tier 2 Zones", count=2))
    if world.options.objective >= 3:
        predreadfell.connect(earlyeast, "Early East/West starting with Dreadfell",
                             Has("Dreadfell") &
                             HasGroupUnique("Tier 2 Zones", count=4) &
                             HasGroupUnique("Pre-Dreadfell Zones", count=2))
    if world.options.objective >= 4:
        earlyeast.connect(prides, "Orc Prides after Tannen", Has("Reknor") & Has("Tannen"))
        prides.connect(endgame, "Endgame after Prides", HasGroupUnique("Pride Zones", count=4))

    for zone in ZONES:
        if zone.required_start and zone.required_start not in world.options.required_starts:
            continue
        zone_region = Region(zone.name, world.player, world.multiworld)
        if zone.tier:
            try:
                parent_region = world.get_region(zone.tier)
            except KeyError:
                # Region should not be in the seed.
                continue
            parent_region.connect(
                zone_region, f"{zone.name} in {zone.tier}", zone.entrance_rule)
        world.multiworld.regions.append(zone_region)

        for enemy in zone.enemies:
            if enemy not in created_regions:
                created_regions.add(enemy)
                enemy_region = Region(enemy, world.player, world.multiworld)
                world.multiworld.regions.append(enemy_region)
            else:
                enemy_region = world.get_region(enemy)
            zone_region.connect(enemy_region, f"{enemy} in {zone.name}")

        if world.options.require_all_zones:
            for enemy_list in zone.variants.values():
                for enemy in enemy_list:
                    if enemy not in created_regions:
                        created_regions.add(enemy)
                        enemy_region = Region(enemy, world.player, world.multiworld)
                        world.multiworld.regions.append(enemy_region)
                    else:
                        enemy_region = world.get_region(enemy)
                    zone_region.connect(enemy_region, f"{enemy} in {zone.name}")

        if zone.has_backup_guardian and world.options.objective >= 3:
            backup_guardian_region = Region(
                f"{zone.name} Backup Guardian", world.player, world.multiworld)
            world.multiworld.regions.append(backup_guardian_region)
            earlyeast.connect(backup_guardian_region,
                              f"{zone.name} Backup Guardian in Early East/West",
                              Has("Reknor") & zone.entrance_rule)

ZONES_BY_NAME = {zone.name: zone for zone in ZONES}
