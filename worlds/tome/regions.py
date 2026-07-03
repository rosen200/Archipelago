from __future__ import annotations
import dataclasses

from typing import TYPE_CHECKING

from BaseClasses import Region
from rule_builder.rules import Has, HasAny, HasGroupUnique, Rule, True_

if TYPE_CHECKING:
    from .world import TOMEWorld


@dataclasses.dataclass
class TOMEZone:
    name: str
    enemies: list[str]
    variant_enemies: list[str]
    tier: str
    entrance_rule: Rule
    has_backup_guardian: bool = False

ZONES = [
    TOMEZone(
        name="Trollmire",
        enemies=["Trolls Tier 1", "Vermin Tier 1", "Snake Tier 1", "Plant Tier 1", "Swarm Tier 1"],
        variant_enemies=["Canines Tier 1", "Aquatic Critter Tier 1", "Bear Tier 1"],
        tier="Tier 1",
        entrance_rule=True_(),
        has_backup_guardian=True,
    ),
    TOMEZone(
        name="Scintillating Caves",
        enemies=["Crystal Tier 1", "Vermin Tier 1", "Snake Tier 1", "Bear Tier 1"],
        variant_enemies=[],
        tier="Tier 1",
        entrance_rule=True_(),
        has_backup_guardian=True,
    ),
    TOMEZone(
        name="Norgos' Lair",
        enemies=["Canines Tier 1", "Vermin Tier 1", "Snake Tier 1", "Bear Tier 1", "Plant Tier 1"],
        variant_enemies=["Shivgoroth Tier 1"],
        tier="Tier 1",
        entrance_rule=True_(),
    ),
    TOMEZone(
        name="Kor'Pul",
        enemies=["Rodent Tier 1", "Vermin Tier 1", "Snake Tier 1", "Molds Tier 1"],
        variant_enemies=["Skeletons Tier 1", "Thieves Tier 1"],
        tier="Tier 1.5",
        entrance_rule=Has("Kor'Pul"),
        has_backup_guardian=True,
    ),
    TOMEZone(
        name="Heart of the Gloom",
        enemies=["Rodent Tier 1", "Vermin Tier 1", "Snake Tier 1", "Plant Tier 1"],
        variant_enemies=[],
        tier="Tier 1.5",
        entrance_rule=Has("Heart of the Gloom")
    ),
    TOMEZone(
        name="Rhaloren Camp",
        enemies=["Elven Warriors Tier 1", "Elven Casters Tier 1"],
        variant_enemies=[],
        tier="Tier 1.5",
        entrance_rule=Has("Rhaloren Camp")
    ),
    TOMEZone(
        name="Old Forest",
        enemies=["Bear Tier 1", "Bear Tier 2", "Ant Tier 1", "Ant Tier 2",
                 "Plant Tier 1", "Plant Tier 2", "Snake Tier 1",
                 "Swarm Tier 1", "Vermin Tier 1"],
        variant_enemies=["Canines Tier 1", "Canines Tier 2", "Crystal Tier 1"],
        tier="Tier 2",
        entrance_rule=Has("Old Forest"),
        has_backup_guardian=True,
    ),
    TOMEZone(
        name="Sandworm Lair",
        # Everything except sandworms is fairly rare in this zone.
        enemies=["Sandworm Tier 1"],
        variant_enemies=[],
        tier="Tier 2",
        entrance_rule=Has("Sandworm Lair"),
        has_backup_guardian=True,
    ),
    TOMEZone(
        name="Maze",
        enemies=["Jelly Tier 1", "Ooze Tier 1", "Ooze Tier 2", "Thieves Tier 1", "Thieves Tier 2"],
        variant_enemies=["Minotaur Tier 2", "Corrupted Horror Tier 1", "Temporal Horror Tier 2"],
        tier="Tier 2",
        entrance_rule=Has("Maze"),
        has_backup_guardian=True,
    ),
    TOMEZone(
        name="Daikara",
        enemies=["Xorn Tier 2", "Snow Giant Tier 2"],
        variant_enemies=["Cold Drake Tier 2", "Fire Drake Tier 2"],
        tier="Tier 2",
        entrance_rule=Has("Daikara") & HasAny("Old Forest", "Maze", "Sandworm Lair"),
        has_backup_guardian=True,
    ),
    TOMEZone(
        name="Stormed Derth",
        enemies=["Gwelgoroth Tier 2"],
        variant_enemies=[],
        tier="Tier 2",
        entrance_rule=True_()
    ),
    TOMEZone(
        name="Ruined Dungeon",
        # Almost any enemy in the game can spawn here.
        # No single enemy is likely enough to be here to consider in logic.
        enemies=[],
        variant_enemies=[],
        tier="Misc Pre-Dreadfell",
        entrance_rule=Has("Ruined Dungeon")
    ),
    TOMEZone(
        name="Halfling Ruins",
        enemies=["Skeletons Tier 1", "Skeletons Tier 2", "Ghoul Tier 1", "Ghoul Tier 2"],
        variant_enemies=[],
        tier="Misc Pre-Dreadfell",
        entrance_rule=Has("Halfling Ruins")
    ),
    TOMEZone(
        name="Ring of Blood",
        enemies=["Slave Tier 2"],
        variant_enemies=[],
        tier="Misc Pre-Dreadfell",
        entrance_rule=Has("Ring of Blood")
    ),
    TOMEZone(
        name="Golem Graveyard",
        enemies=["Golem Tier 1", "Golem Tier 2",],
        variant_enemies=[],
        tier="Misc Pre-Dreadfell",
        entrance_rule=Has("Golem Graveyard")
    ),
    TOMEZone(
        name="Lake of Nur",
        enemies=["Aquatic Critter Tier 1", "Aquatic Critter Tier 2",
                 "Aquatic Demon Tier 2"],
        variant_enemies=["Snake Tier 1", "Plant Tier 1", "Plant Tier 2",
                         "Horror Tier 3", "Horror Tier 2",
                         "Aquatic Horror Tier 2"],
        tier="Misc Pre-Dreadfell",
        entrance_rule=Has("Old Forest")
    ),
    TOMEZone(
        name="Mark of the Spellblaze",
        enemies=["Elven Casters Tier 1", "Elven Casters Tier 3",
                 "Faeros Tier 3", "Gwelgoroth Tier 2"],
        variant_enemies=[],
        tier="Misc Pre-Dreadfell",
        entrance_rule=Has("Mark of the Spellblaze")
    ),
    TOMEZone(
        name="Tempest Peak",
        enemies=["Gwelgoroth Tier 2", "Xorn Tier 2", "Snow Giant Tier 2",
                 "Storm Drake Tier 2"],
        variant_enemies=[],
        tier="Misc Pre-Dreadfell",
        entrance_rule=True_(),
    ),
    TOMEZone(
        name="Temporal Rift",
        enemies=["Temporal Horror Tier 2", "Temporal Horror Tier 3",
                 "Telugoroth Tier 2", "Telugoroth Tier 3"],
        variant_enemies=[],
        tier="Misc Pre-Dreadfell",
        entrance_rule=Has("Daikara"),
    ),
    TOMEZone(
        name="Last Hope Graveyard",
        # Only bosses
        enemies=[],
        variant_enemies=[],
        tier="Misc Pre-Dreadfell",
        entrance_rule=True_(),
    ),
    TOMEZone(
        name="Dreadfell",
        enemies=["Skeletons Tier 1", "Skeletons Tier 2", "Ghoul Tier 1",
                 "Ghoul Tier 2", "Vampire Tier 2", "Vampire Tier 3",
                 "Wight Tier 2", "Wight Tier 3"],
        variant_enemies=[],
        tier="Early East/West",
        # Dreadfell item is required by parent region
        entrance_rule=True_(),
        has_backup_guardian=True,
    ),
    TOMEZone(
        name="Reknor",
        enemies=["Trolls Tier 1", "Trolls Tier 2", "Orc Tier 1", "Orc Tier 2"],
        variant_enemies=[],
        tier="Early East/West",
        entrance_rule=Has("Reknor"),
        has_backup_guardian=True,
    ),
    TOMEZone(
        name="Briagh's Lair",
        enemies=["Sandworm Tier 1", "Sandworm Tier 3"],
        variant_enemies=[],
        tier="Early East/West",
        entrance_rule=Has("Reknor")
    ),
    TOMEZone(
        name="Vor Armoury",
        enemies=["Orc Tier 1", "Orc Tier 2", "Vor Orc Tier 4"],
        variant_enemies=[],
        tier="Early East/West",
        entrance_rule=Has("Reknor")
    ),
    TOMEZone(
        name="Unremarkable Cave",
        enemies=["Rodent Tier 1", "Vermin Tier 1", "Molds Tier 1",
                 "Snake Tier 1", "Skeletons Tier 1", "Skeletons Tier 2"],
        variant_enemies=[],
        tier="Early East/West",
        entrance_rule=Has("Reknor")
    ),
    TOMEZone(
        name="Ardhungol",
        enemies=["Spider Tier 1", "Spider Tier 2", "Spider Tier 4"],
        variant_enemies=[],
        tier="Early East/West",
        entrance_rule=Has("Reknor") & Has("Ardhungol")
    ),
    TOMEZone(
        name="Tannen's Quest",
        enemies=[],
        # These are technically two mutually exclusive zones, but for
        # logic purposes they work well being treated as an alt
        # versions with no overlap.
        variant_enemies=["Skeletons Tier 1", "Skeletons Tier 2",
                         "Ghoul Tier 1", "Ghoul Tier 2",
                         "Bone Giant Tier 3", "Bone Giant Tier 4",
                         "Minor Demon Tier 2", "Minor Demon Tier 3",
                         "Major Demon Tier 4"],
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
        variant_enemies=[],
        tier="Early East/West",
        entrance_rule=Has("Reknor") & Has("Tannen")
    ),
    TOMEZone(
        name="Flooded Cave",
        enemies=["Aquatic Critter Tier 1", "Aquatic Critter Tier 2", "Aquatic Demon Tier 2"],
        variant_enemies=[],
        tier="Early East/West",
        entrance_rule=Has("Reknor") & Has("Flooded Cave")
    ),
    TOMEZone(
        name="Temple of Creation",
        enemies=["Naga Tier 4", "Naga Tier 5"],
        variant_enemies=[],
        tier="Early East/West",
        entrance_rule=Has("Reknor") & Has("Flooded Cave")
    ),
]

def create_and_connect_regions(world: TOMEWorld) -> None:
    created_regions = set()
    # Create and connect the tier containers
    eyal = Region("Maj'Eyal", world.player, world.multiworld)
    tier1 = Region("Tier 1", world.player, world.multiworld)
    tier15 = Region("Tier 1.5", world.player, world.multiworld)
    tier2 = Region("Tier 2", world.player, world.multiworld)
    predreadfell = Region("Misc Pre-Dreadfell", world.player, world.multiworld)
    earlyeast = Region("Early East/West", world.player, world.multiworld)
    regions = [eyal, tier1, tier15, tier2, predreadfell, earlyeast]
    world.multiworld.regions += regions

    eyal.connect(tier1, "Eyal to Tier 1")
    tier1.connect(tier15, "Tier 1 to Tier 1.5")
    tier15.connect(tier2, "Tier 1.5 to Tier 2", HasGroupUnique("Tier 1.5 Zones", count=1))
    tier2.connect(predreadfell, "Tier 2 to Pre-Dreadfell", HasGroupUnique("Tier 2 Zones", count=3))
    predreadfell.connect(earlyeast, "Early East/West starting with Dreadfell",
                         Has("Dreadfell") &
                         HasGroupUnique("Tier 2 Zones", count=4) &
                         HasGroupUnique("Pre-Dreadfell Zones", count=2))

    for zone in ZONES:
        zone_region = Region(zone.name, world.player, world.multiworld)
        if zone.tier:
            world.get_region(zone.tier).connect(
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

        if world.options.require_alt_zones:
            for enemy in zone.variant_enemies:
                if enemy not in created_regions:
                    created_regions.add(enemy)
                    enemy_region = Region(enemy, world.player, world.multiworld)
                    world.multiworld.regions.append(enemy_region)
                else:
                    enemy_region = world.get_region(enemy)
                zone_region.connect(enemy_region, f"{enemy} in {zone.name}")

        if zone.has_backup_guardian:
            backup_guardian_region = Region(
                f"{zone.name} Backup Guardian", world.player, world.multiworld)
            world.multiworld.regions.append(backup_guardian_region)
            earlyeast.connect(backup_guardian_region,
                              f"{zone.name} Backup Guardian in Early East/West",
                              Has("Reknor") & zone.entrance_rule)
