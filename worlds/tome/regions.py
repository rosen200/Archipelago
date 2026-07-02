from __future__ import annotations
import dataclasses

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region
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

ZONES = [
    TOMEZone(
        name="Trollmire",
        enemies=["Trolls Tier 1", "Vermin Tier 1", "Snake Tier 1", "Plant Tier 1", "Swarm Tier 1"],
        variant_enemies=["Canines Tier 1", "Aquatic Critter Tier 1", "Bear Tier 1"],
        tier="Tier 1",
        entrance_rule=True_()
    ),
    TOMEZone(
        name="Scintillating Caves",
        enemies=["Crystal Tier 1", "Vermin Tier 1", "Snake Tier 1", "Bear Tier 1"],
        variant_enemies=[],
        tier="Tier 1",
        entrance_rule=True_(),
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
        entrance_rule=Has("Kor'Pul")
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
        enemies=["Bear Tier 1", "Bear Tier 2", "Ant Tier 1", "Ant Tier 2", "Plant Tier 1", "Plant Tier 2", "Snake Tier 1", "Swarm Tier 1", "Vermin Tier 1"],
        variant_enemies=["Canines Tier 1", "Canines Tier 2", "Crystal Tier 1"],
        tier="Tier 2",
        entrance_rule=Has("Old Forest")
    ),
    TOMEZone(
        name="Sandworm Lair",
        # Everything except sandworms is fairly rare in this zone.
        enemies=["Sandworm Tier 1"],
        variant_enemies=[],
        tier="Tier 2",
        entrance_rule=Has("Sandworm Lair")
    ),
    TOMEZone(
        name="Maze",
        enemies=["Jelly Tier 1", "Ooze Tier 1", "Ooze Tier 2", "Thieves Tier 1", "Thieves Tier 2"],
        variant_enemies=["Minotaur Tier 2", "Corrupted Horror Tier 1", "Temporal Horror Tier 2"],
        tier="Tier 2",
        entrance_rule=Has("Maze")
    ),
    TOMEZone(
        name="Daikara",
        enemies=["Xorn Tier 2", "Snow Giant Tier 2"],
        variant_enemies=["Cold Drake Tier 2", "Fire Drake Tier 2"],
        tier="Tier 2",
        entrance_rule=Has("Daikara") & HasAny("Old Forest", "Maze", "Sandworm Lair")
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
        enemies=["Aquatic Critter Tier 1", "Aquatic Critter Tier 2", "Aquatic Demon Tier 2"],
        variant_enemies=["Snake Tier 1", "Plant Tier 1", "Plant Tier 2", "Horror Tier 3", "Horror Tier 2", "Aquatic Horror Tier 2"],
        tier="Misc Pre-Dreadfell",
        entrance_rule=Has("Old Forest")
    ),
    TOMEZone(
        name="Mark of the Spellblaze",
        enemies=["Elven Casters Tier 1", "Elven Casters Tier 3", "Faeros Tier 3", "Gwelgoroth Tier 2"],
        variant_enemies=[],
        tier="Misc Pre-Dreadfell",
        entrance_rule=Has("Mark of the Spellblaze")
    ),
    TOMEZone(
        name="Tempest Peak",
        enemies=["Gwelgoroth Tier 2", "Xorn Tier 2", "Snow Giant Tier 2", "Storm Drake Tier 2"],
        variant_enemies=[],
        tier="Misc Pre-Dreadfell",
        entrance_rule=True_(),
    ),
    TOMEZone(
        name="Dreadfell",
        enemies=["Skeletons Tier 1", "Skeletons Tier 2", "Ghoul Tier 1", "Ghoul Tier 2", "Vampire Tier 2", "Vampire Tier 3", "Wight Tier 2", "Wight Tier 3"],
        variant_enemies=[],
        tier="Misc Pre-Dreadfell",
        entrance_rule=Has("Dreadfell") & HasGroupUnique("Tier 2 Zones", count=4) & HasGroupUnique("Pre-Dreadfell Zones", count=2)
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
    regions = [eyal, tier1, tier15, tier2, predreadfell]
    world.multiworld.regions += regions

    
    eyal.connect(tier1, "Eyal to Tier 1")
    tier1.connect(tier15, "Tier 1 to Tier 1.5")
    tier15.connect(tier2, "Tier 1.5 to Tier 2", HasGroupUnique("Tier 1.5 Zones", count=1))
    tier2.connect(predreadfell, "Tier 2 to Pre-Dreadfell", HasGroupUnique("Tier 2 Zones", count=3))
    
    for zone in ZONES:
        zone_region = Region(zone.name, world.player, world.multiworld)
        if zone.tier:
            world.get_region(zone.tier).connect(zone_region, f"{zone.name} in {zone.tier}", zone.entrance_rule)
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
        

def create_all_regions(world: TOMEWorld) -> None:
    # Creating a region is as simple as calling the constructor of the Region class.
    eyal = Region("Maj'Eyal", world.player, world.multiworld)
    tier1 = Region("Tier 1", world.player, world.multiworld)
    trollmire = Region("Trollmire", world.player, world.multiworld)
    cave = Region("Scintillating Caves", world.player, world.multiworld)
    norgos = Region("Norgos' Lair", world.player, world.multiworld)
    tier15 = Region("Tier 1.5", world.player, world.multiworld)
    korpul = Region("Kor'Pul", world.player, world.multiworld)
    rhaloren = Region("Rhaloren Camp", world.player, world.multiworld)
    gloom = Region("Heart of the Gloom", world.player, world.multiworld)
    tier2 = Region("Tier 2", world.player, world.multiworld)
    forest = Region("Old Forest", world.player, world.multiworld)
    sandworm_lair = Region("Sandworm Lair", world.player, world.multiworld)
    maze = Region("Maze", world.player, world.multiworld)
    daikara = Region("Daikara", world.player, world.multiworld)
    predreadfell = Region("Misc Pre-Dreadfell", world.player, world.multiworld)
    hidden_compound = Region("Hidden Compound", world.player, world.multiworld)
    ruined_dungeon = Region("Ruined Dungeon", world.player, world.multiworld)
    halfling_ruins = Region("Halfling Ruins", world.player, world.multiworld)
    spellblaze = Region("Mark of the Spellblaze", world.player, world.multiworld)
    nur = Region("Lake of Nur", world.player, world.multiworld)
    dreadfell = Region("Dreadfell", world.player, world.multiworld)
    trolls_lowlevel = Region("Low Level Trolls", world.player, world.multiworld)
    undead_lowlevel = Region("Low Level Undead", world.player, world.multiworld)
    animals_lowlevel = Region("Low Level Animals", world.player, world.multiworld)
    immobile_lowlevel = Region("Low Level Immobiles", world.player, world.multiworld)
    humanoids_lowlevel = Region("Low Level Humanoids", world.player, world.multiworld)

    # Let's put all these regions in a list.
    regions = [eyal, tier1, trollmire, cave, norgos, tier15, korpul, rhaloren, gloom, tier2, forest, sandworm_lair, maze, daikara, predreadfell, hidden_compound, ruined_dungeon, halfling_ruins, spellblaze, dreadfell, trolls_lowlevel, undead_lowlevel, animals_lowlevel, immobile_lowlevel, humanoids_lowlevel]
    world.multiworld.regions += regions

def connect_regions(world: TOMEWorld) -> None:
    # We have regions now, but still need to connect them to each other.
    # But wait, we no longer have access to the region variables we created in create_all_regions()!
    # Luckily, once you've submitted your regions to multiworld.regions,
    # you can get them at any time using world.get_region(...).
    eyal = world.get_region("Maj'Eyal")
    tier1 = world.get_region("Tier 1")
    trollmire = world.get_region("Trollmire")
    cave = world.get_region("Scintillating Caves")
    norgos = world.get_region("Norgos' Lair")
    tier15 = world.get_region("Tier 1.5")
    korpul = world.get_region("Kor'Pul")
    rhaloren = world.get_region("Rhaloren Camp")
    gloom = world.get_region("Heart of the Gloom")
    tier2 = world.get_region("Tier 2")
    forest = world.get_region("Old Forest")
    sandworm_lair = world.get_region("Sandworm Lair")
    maze = world.get_region("Maze")
    daikara = world.get_region("Daikara")
    predreadfell = world.get_region("Misc Pre-Dreadfell")
    hidden_compound = world.get_region("Hidden Compound")
    ruined_dungeon = world.get_region("Ruined Dungeon")
    halfling_ruins = world.get_region("Halfling Ruins")
    spellblaze = world.get_region("Mark of the Spellblaze")
    nur = world.get_region("Lake of Nur")
    dreadfell = world.get_region("Dreadfell")
    trolls_lowlevel = world.get_region("Low Level Trolls")
    undead_lowlevel = world.get_region("Low Level Undead")
    animals_lowlevel = world.get_region("Low Level Animals")
    immobile_lowlevel = world.get_region("Low Level Immobiles")
    humanoids_lowlevel = world.get_region("Low Level Humanoids")

    eyal.connect(tier1, "Eyal to Tier 1")
    tier1.connect(trollmire, "Trollmire in Tier 1")
    trollmire.connect(trolls_lowlevel, "Low-Level Trolls in Trollmire")
    trollmire.connect(animals_lowlevel, "Low-Level Animals in Trollmire")
    tier1.connect(cave, "Scintillating Caves in Tier 1")
    cave.connect(immobile_lowlevel, "Low-Level Immobiles in Scintillating Caves")
    tier1.connect(norgos, "Norgos' Lair in Tier 1")
    trollmire.connect(animals_lowlevel, "Low-Level Animals in Norgos' Lair")
    tier1.connect(tier15, "Tier 1 to Tier 1.5")
    
    tier15.connect(korpul, "Kor'Pul in Tier 1.5", Has("Kor'Pul"))
    korpul.connect(humanoids_lowlevel, "Low-Level Humanoids in Kor'Pul")
    korpul.connect(undead_lowlevel, "Low-Level Undead in Kor'Pul")
    tier15.connect(rhaloren, "Rhaloren Camp in Tier 1.5", Has("Rhaloren Camp"))
    tier15.connect(gloom, "Heart of the Gloom in Tier 1.5", Has("Heart of the Gloom"))
    tier15.connect(tier2, "Tier 1.5 to Tier 2", HasGroupUnique("Tier 1.5 Zones", count=1))
    
    tier2.connect(forest, "Old Forest in Tier 2", Has("Old Forest"))
    tier2.connect(maze, "Maze in Tier 2", Has("Maze"))
    tier2.connect(sandworm_lair, "Sandworm Lair in Tier 2", Has("Sandworm Lair"))
    # Daikara is harder than the other tier 2 zones, ensure the player can do another one first
    tier2.connect(daikara, "Daikara in Tier 2", Has("Daikara") & HasAny("Old Forest", "Maze", "Sandworm Lair"))
    tier2.connect(predreadfell, "Tier 2 to Pre-Dreadfell", HasGroupUnique("Tier 2 Zones", count=3))
    
    predreadfell.connect(hidden_compound, "Hidden Compound before Dreadfell", Has("Ring of Blood"))
    predreadfell.connect(halfling_ruins, "Halfling Ruins before Dreadfell", Has("Halfling Ruins"))
    predreadfell.connect(ruined_dungeon, "Ruined Dungeon before Dreadfell", Has("Ruined Dungeon"))
    # This zone is reached through the old forest, but difficulty wise
    # is closer to pre-dreadfell zones
    predreadfell.connect(nur, "Lake of Nur before Dreadfell", Has("Old Forest"))
    # Much like Daikara this zone is a lot harder than others in the same tier
    predreadfell.connect(spellblaze, "Mark of the Spellblaze before Dreadfell", Has("Mark of the Spellblaze") & (HasGroupUnique("Tier 2 Zones", count=4) | HasAny("Ring of Blood", "Halfling Ruins", "Ruined Dungeon")))
    predreadfell.connect(dreadfell, "Dreadfell entrance", Has("Dreadfell") & HasGroupUnique("Tier 2 Zones", count=4) & HasGroupUnique("Pre-Dreadfell Zones", count=2))
