from __future__ import annotations
import dataclasses

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import TOMEWorld


@dataclasses.dataclass
class TOMEItemDef():
    name: str
    ap_id: int
    classification: ItemClassification
    minimum_goal: int

TOME_ITEMS = {
    "Kor'Pul": TOMEItemDef(
        name="Kor'Pul",
        ap_id=1,
        classification=ItemClassification.progression,
        minimum_goal=0
    ),
    "Rhaloren Camp": TOMEItemDef(
        name="Rhaloren Camp",
        ap_id=2,
        classification=ItemClassification.progression,
        minimum_goal=0
    ),
    "Heart of the Gloom": TOMEItemDef(
        name="Heart of the Gloom",
        ap_id=3,
        classification=ItemClassification.progression,
        minimum_goal=0
    ),
    "Old Forest": TOMEItemDef(
        name="Old Forest",
        ap_id=4,
        classification=ItemClassification.progression,
        minimum_goal=1
    ),
    "Maze": TOMEItemDef(
        name="Maze",
        ap_id=5,
        classification=ItemClassification.progression,
        minimum_goal=1
    ),
    "Sandworm Lair": TOMEItemDef(
        name="Sandworm Lair",
        ap_id=6,
        classification=ItemClassification.progression,
        minimum_goal=1
    ),
    "Daikara": TOMEItemDef(
        name="Daikara",
        ap_id=7,
        classification=ItemClassification.progression,
        minimum_goal=1
    ),
    "Ruined Dungeon": TOMEItemDef(
        name="Ruined Dungeon",
        ap_id=8,
        classification=ItemClassification.progression,
        minimum_goal=2
    ),
    "Ring of Blood": TOMEItemDef(
        name="Ring of Blood",
        ap_id=9,
        classification=ItemClassification.progression,
        minimum_goal=2
    ),
    "Mark of the Spellblaze": TOMEItemDef(
        name="Mark of the Spellblaze",
        ap_id=10,
        classification=ItemClassification.progression,
        minimum_goal=2
    ),
    "Halfling Ruins": TOMEItemDef(
        name="Halfling Ruins",
        ap_id=11,
        classification=ItemClassification.progression,
        minimum_goal=2
    ),
    "Golem Graveyard": TOMEItemDef(
        name="Golem Graveyard",
        ap_id=12,
        classification=ItemClassification.progression,
        minimum_goal=2
    ),
    "Dreadfell": TOMEItemDef(
        name="Dreadfell",
        ap_id=13,
        classification=ItemClassification.progression,
        minimum_goal=2
    ),
    "Tale of Maj'Eyal": TOMEItemDef(
        name="Tale of Maj'Eyal",
        ap_id=14,
        classification=ItemClassification.progression_deprioritized_skip_balancing,
        minimum_goal=0
    ),
    "20 Gold": TOMEItemDef(
        name="20 Gold",
        ap_id=15,
        classification=ItemClassification.filler,
        minimum_goal=0
    ),
    "Random Artifact": TOMEItemDef(
        name="Random Artifact",
        ap_id=16,
        classification=ItemClassification.filler,
        minimum_goal=0
    ),
    "Extra Life": TOMEItemDef(
        name="Extra Life",
        ap_id=17,
        classification=ItemClassification.useful,
        minimum_goal=0
    ),
    "Stat Point": TOMEItemDef(
        name="Stat Point",
        ap_id=18,
        classification=ItemClassification.filler,
        minimum_goal=0
    ),
    "Generic Talent Point": TOMEItemDef(
        name="Generic Talent Point",
        ap_id=19,
        classification=ItemClassification.useful,
        minimum_goal=0
    ),
    "Class Talent Point": TOMEItemDef(
        name="Class Talent Point",
        ap_id=20,
        classification=ItemClassification.useful,
        minimum_goal=0
    ),
    "Category Talent Point": TOMEItemDef(
        name="Category Talent Point",
        ap_id=21,
        classification=ItemClassification.useful,
        minimum_goal=0
    ),
    "Prodigy Point": TOMEItemDef(
        name="Prodigy Point",
        ap_id=22,
        classification=ItemClassification.useful,
        minimum_goal=0
    ),
}

ITEM_NAME_TO_ID = {name: item.ap_id for name, item in TOME_ITEMS.items()}

ITEM_GROUPS = {
    "Tier 1.5 Zones": set({"Kor'Pul", "Rhaloren Camp", "Heart of the Gloom"}),
    "Tier 2 Zones": set({"Old Forest", "Maze", "Sandworm Lair", "Daikara"}),
    "Pre-Dreadfell Zones": set({"Ruined Dungeon", "Ring of Blood",
                                "Mark of the Spellblaze", "Halfling Ruins"}),
    "Talent Points": set({"Generic Talent Point", "Class Talent Point",
                          "Category Talent Point", "Prodigy Point"}),
}

class TOMEItem(Item):
    game = "TOME"


def get_random_filler_item_name(world: TOMEWorld) -> str:
    if world.random.randint(0, 2) == 0:
        return "Random Artifact"
    return "20 Gold"


def create_item_with_correct_classification(world: TOMEWorld, name: str) -> TOMEItem:
    classification = TOME_ITEMS[name].classification
    return TOMEItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: TOMEWorld) -> None:
    itempool: list[Item] = [
        item.name for item in TOME_ITEMS.values()
        if item.minimum_goal <= world.options.objective
        and item.classification == ItemClassification.progression
    ]
    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    open_items = number_of_unfilled_locations - number_of_items

    if open_items and world.options.include_prodigy and world.options.objective >= 2:
        open_items -= 1
        itempool.append("Prodigy Point")
    if open_items and world.options.include_category_point:
        open_items -= 1
        itempool.append("Category Talent Point")
    if open_items and world.options.num_class_points > 0:
        num_class_points = min(world.options.num_class_points, open_items)
        open_items -= num_class_points
        itempool.extend(["Class Talent Point"] * num_class_points)
    if open_items and world.options.num_generic_points > 0:
        num_generic_points = min(world.options.num_generic_points, open_items)
        open_items -= num_generic_points
        itempool.extend(["Generic Talent Point"] * num_generic_points)
    if open_items and world.options.num_extra_lives > 0:
        num_extra_lives = min(world.options.num_extra_lives, open_items)
        open_items -= num_extra_lives
        itempool.extend(["Extra Life"] * num_extra_lives)
    if open_items and world.options.num_stat_points > 0:
        num_stat_points = min(world.options.num_stat_points, open_items)
        open_items -= num_stat_points
        itempool.extend(["Stat Point"] * num_stat_points)

    itempool = [world.create_item(item) for item in itempool]
    itempool += [world.create_filler() for _ in range(open_items)]
    world.multiworld.itempool += itempool
