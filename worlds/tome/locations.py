from __future__ import annotations
import dataclasses

from typing import TYPE_CHECKING

from BaseClasses import Location

from . import items

if TYPE_CHECKING:
    from .world import TOMEWorld


@dataclasses.dataclass
class TomeEnemyLocation:
    name: str
    ap_id: int
    region: str
    is_boss: bool
    minimum_goal: int


ENEMY_LOCATIONS = {
    # Note that regular enemy names are all lowercase
    "stone troll": TomeEnemyLocation(
        name="stone troll",
        ap_id=1,
        region="Trolls Tier 1",
        is_boss=False,
        minimum_goal=0,
    ),
    "forest troll": TomeEnemyLocation(
        name="forest troll",
        ap_id=2,
        region="Trolls Tier 1",
        is_boss=False,
        minimum_goal=0,
    ),
    "cave troll": TomeEnemyLocation(
        name="cave troll",
        ap_id=3,
        region="Trolls Tier 1",
        is_boss=False,
        minimum_goal=0,
    ),
    # Mountain troll is too rare before Reknor
    "wolf": TomeEnemyLocation(
        name="wolf",
        ap_id=4,
        region="Canines Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "great wolf": TomeEnemyLocation(
        name="great wolf",
        ap_id=5,
        region="Canines Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "dire wolf": TomeEnemyLocation(
        name="dire wolf",
        ap_id=6,
        region="Canines Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "white wolf": TomeEnemyLocation(
        name="white wolf",
        ap_id=7,
        region="Canines Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    # Rarity 4, but canines appear in so many zones players usually
    # find one by old forest
    "warg": TomeEnemyLocation(
        name="warg",
        ap_id=8,
        region="Canines Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "white worm mass": TomeEnemyLocation(
        name="white worm mass",
        ap_id=9,
        region="Vermin Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "green worm mass": TomeEnemyLocation(
        name="green worm mass",
        ap_id=10,
        region="Vermin Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "large white snake": TomeEnemyLocation(
        name="large white snake",
        ap_id=11,
        region="Snake Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "large brown snake": TomeEnemyLocation(
        name="large brown snake",
        ap_id=102,
        region="Snake Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "copperhead snake": TomeEnemyLocation(
        name="copperhead snake",
        ap_id=12,
        region="Snake Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "rattlesnake": TomeEnemyLocation(
        name="rattlesnake",
        ap_id=13,
        region="Snake Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "midge swarm": TomeEnemyLocation(
        name="midge swarm",
        ap_id=14,
        region="Swarm Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "bee swarm": TomeEnemyLocation(
        name="bee swarm",
        ap_id=15,
        region="Swarm Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "hornet swarm": TomeEnemyLocation(
        name="midge swarm",
        ap_id=16,
        region="Swarm Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "giant venus flytrap": TomeEnemyLocation(
        name="giant venus flytrap",
        ap_id=17,
        region="Plant Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "treant": TomeEnemyLocation(
        name="treant",
        ap_id=18,
        region="Plant Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "poison ivy": TomeEnemyLocation(
        name="poison ivy",
        ap_id=19,
        region="Plant Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "honey tree": TomeEnemyLocation(
        name="honey tree",
        ap_id=20,
        region="Plant Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "brown bear": TomeEnemyLocation(
        name="brown bear",
        ap_id=21,
        region="Bear Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "black bear": TomeEnemyLocation(
        name="black bear",
        ap_id=103,
        region="Bear Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "cave bear": TomeEnemyLocation(
        name="cave bear",
        ap_id=22,
        region="Bear Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "war bear": TomeEnemyLocation(
        name="war bear",
        ap_id=23,
        region="Bear Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "grizzly bear": TomeEnemyLocation(
        name="grizzly bear",
        ap_id=24,
        region="Bear Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "polar bear": TomeEnemyLocation(
        name="polar bear",
        ap_id=25,
        region="Bear Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "giant white mouse": TomeEnemyLocation(
        name="giant white mouse",
        ap_id=26,
        region="Rodent Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "giant brown mouse": TomeEnemyLocation(
        name="giant brown mouse",
        ap_id=27,
        region="Rodent Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "giant white rat": TomeEnemyLocation(
        name="giant white rat",
        ap_id=28,
        region="Rodent Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "giant brown rat": TomeEnemyLocation(
        name="giant brown rat",
        ap_id=29,
        region="Rodent Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "giant rabbit": TomeEnemyLocation(
        name="giant rabbit",
        ap_id=30,
        region="Rodent Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "giant crystal rat": TomeEnemyLocation(
        name="giant crystal rat",
        ap_id=104,
        region="Rodent Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "giant grey mouse": TomeEnemyLocation(
        name="giant brown mouse",
        ap_id=31,
        region="Rodent Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "giant grey rat": TomeEnemyLocation(
        name="giant white rat",
        ap_id=32,
        region="Rodent Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "giant eel": TomeEnemyLocation(
        name="giant eel",
        ap_id=33,
        region="Aquatic Critter Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    # Squid could spawn in tier 1, but the only tier 1 zone that has
    # aquatic critters explicitly bans them from spawning.
    "squid": TomeEnemyLocation(
        name="squid",
        ap_id=34,
        region="Aquatic Critter Tier 2",
        is_boss=False,
        minimum_goal=2
    ),
    "ink squid": TomeEnemyLocation(
        name="ink squid",
        ap_id=35,
        region="Aquatic Critter Tier 2",
        is_boss=False,
        minimum_goal=2
    ),
    "red crystal": TomeEnemyLocation(
        name="red crystal",
        ap_id=36,
        region="Crystal Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "white crystal": TomeEnemyLocation(
        name="white crystal",
        ap_id=37,
        region="Crystal Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "black crystal": TomeEnemyLocation(
        name="black crystal",
        ap_id=38,
        region="Crystal Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "crimson crystal": TomeEnemyLocation(
        name="crimson crystal",
        ap_id=39,
        region="Crystal Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "blue crystal": TomeEnemyLocation(
        name="blue crystal",
        ap_id=40,
        region="Crystal Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "multi-hued crystal": TomeEnemyLocation(
        name="multi-hued crystal",
        ap_id=41,
        region="Crystal Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "shimmering crystal": TomeEnemyLocation(
        name="shimmering crystal",
        ap_id=42,
        region="Crystal Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "shivgoroth": TomeEnemyLocation(
        name="shivgoroth",
        ap_id=43,
        region="Shivgoroth Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "greater shivgoroth": TomeEnemyLocation(
        name="greater shivgoroth",
        ap_id=106,
        region="Shivgoroth Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    # Bosses, unlike regular enemies, have title case names.
    "Prox the Mighty": TomeEnemyLocation(
        name="Prox the Mighty",
        ap_id=44,
        region="Trollmire",
        is_boss=True,
        minimum_goal=0
    ),
    "Shax the Slimy": TomeEnemyLocation(
        name="Shax the Slimy",
        ap_id=45,
        region="Trollmire",
        is_boss=True,
        minimum_goal=0
    ),
    "Spellblaze Crystal": TomeEnemyLocation(
        name="Spellblaze Crystal",
        ap_id=46,
        region="Scintillating Caves",
        is_boss=True,
        minimum_goal=0
    ),
    "Norgos, the Guardian": TomeEnemyLocation(
        name="Norgos, the Guardian",
        ap_id=47,
        region="Norgos' Lair",
        is_boss=True,
        minimum_goal=0
    ),
    "Norgos, the Frozen": TomeEnemyLocation(
        name="Norgos, the Frozen",
        ap_id=48,
        region="Norgos' Lair",
        is_boss=True,
        minimum_goal=0
    ),
    "The Shade": TomeEnemyLocation(
        name="The Shade",
        ap_id=49,
        region="Kor'Pul",
        is_boss=True,
        minimum_goal=0
    ),
    "The Possessed": TomeEnemyLocation(
        name="The Possessed",
        ap_id=50,
        region="Kor'Pul",
        is_boss=True,
        minimum_goal=0
    ),
    "degenerated skeleton warrior": TomeEnemyLocation(
        name="degenerated skeleton warrior",
        ap_id=51,
        region="Skeletons Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "degenerated skeleton archer": TomeEnemyLocation(
        name="degenerated skeleton archer",
        ap_id=52,
        region="Skeletons Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "skeleton mage": TomeEnemyLocation(
        name="skeleton mage",
        ap_id=53,
        region="Skeletons Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "skeleton warrior": TomeEnemyLocation(
        name="skeleton warrior",
        ap_id=54,
        region="Skeletons Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "skeleton archer": TomeEnemyLocation(
        name="skeleton archer",
        ap_id=55,
        region="Skeletons Tier 2",
        is_boss=False,
        minimum_goal=2
    ),
    "skeleton magus": TomeEnemyLocation(
        name="skeleton magus",
        ap_id=56,
        region="Skeletons Tier 2",
        is_boss=False,
        minimum_goal=2
    ),
    # Rarity 5, but still quite common
    "armoured skeleton warrior": TomeEnemyLocation(
        name="armoured skeleton warrior",
        ap_id=57,
        region="Skeletons Tier 2",
        is_boss=False,
        minimum_goal=2
    ),
    "skeleton master archer": TomeEnemyLocation(
        name="skeleton master archer",
        ap_id=58,
        region="Skeletons Tier 2",
        is_boss=False,
        minimum_goal=2
    ),
    "The Withering Thing": TomeEnemyLocation(
        name="The Withering Thing",
        ap_id=59,
        region="Heart of the Gloom",
        is_boss=True,
        minimum_goal=0
    ),
    "The Dreaming One": TomeEnemyLocation(
        name="The Dreaming One",
        ap_id=105,
        region="Heart of the Gloom",
        is_boss=True,
        minimum_goal=0
    ),
    "Rhaloren Inquisitor": TomeEnemyLocation(
        name="Rhaloren Inquisitor",
        ap_id=60,
        region="Rhaloren Camp",
        is_boss=True,
        minimum_goal=0
    ),
    "grey mold": TomeEnemyLocation(
        name="grey mold",
        ap_id=61,
        region="Molds Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "brown mold": TomeEnemyLocation(
        name="brown mold",
        ap_id=62,
        region="Molds Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "shining mold": TomeEnemyLocation(
        name="shining mold",
        ap_id=63,
        region="Molds Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "green mold": TomeEnemyLocation(
        name="green mold",
        ap_id=64,
        region="Molds Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "elven guard": TomeEnemyLocation(
        name="elven guard",
        ap_id=65,
        region="Elven Warriors Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "mean looking elven guard": TomeEnemyLocation(
        name="mean looking elven guard",
        ap_id=66,
        region="Elven Warriors Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "elven warrior": TomeEnemyLocation(
        name="elven warrior",
        ap_id=67,
        region="Elven Warriors Tier 2",
        is_boss=False,
        minimum_goal=3
    ),
    "elven elite warrior": TomeEnemyLocation(
        name="elven elite warrior",
        ap_id=68,
        region="Elven Warriors Tier 2",
        is_boss=False,
        minimum_goal=3
    ),
    "elven mage": TomeEnemyLocation(
        name="elven mage",
        ap_id=69,
        region="Elven Casters Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "elven tempest": TomeEnemyLocation(
        name="elven tempest",
        ap_id=70,
        region="Elven Casters Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "cutpurse": TomeEnemyLocation(
        name="cutpurse",
        ap_id=98,
        region="Thieves Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "rogue": TomeEnemyLocation(
        name="cutpurse",
        ap_id=99,
        region="Thieves Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "thief": TomeEnemyLocation(
        name="thief",
        ap_id=100,
        region="Thieves Tier 1",
        is_boss=False,
        minimum_goal=0
    ),
    "assassin": TomeEnemyLocation(
        name="assassin",
        ap_id=101,
        region="Thieves Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "giant white ant": TomeEnemyLocation(
        name="giant white ant",
        ap_id=191,
        region="Ant Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "giant brown ant": TomeEnemyLocation(
        name="giant brown ant",
        ap_id=107,
        region="Ant Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "giant carpenter ant": TomeEnemyLocation(
        name="giant carpenter ant",
        ap_id=108,
        region="Ant Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "giant green ant": TomeEnemyLocation(
        name="giant green ant",
        ap_id=109,
        region="Ant Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "giant red ant": TomeEnemyLocation(
        name="giant red ant",
        ap_id=110,
        region="Ant Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "giant blue ant": TomeEnemyLocation(
        name="giant blue ant",
        ap_id=111,
        region="Ant Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "giant yellow ant": TomeEnemyLocation(
        name="giant yellow ant",
        ap_id=112,
        region="Ant Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "giant black ant": TomeEnemyLocation(
        name="giant black ant",
        ap_id=113,
        region="Ant Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "giant fire ant": TomeEnemyLocation(
        name="giant fire ant",
        ap_id=114,
        region="Ant Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "giant ice ant": TomeEnemyLocation(
        name="giant ice ant",
        ap_id=115,
        region="Ant Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "giant lightning ant": TomeEnemyLocation(
        name="giant lightning ant",
        ap_id=116,
        region="Ant Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "giant acid ant": TomeEnemyLocation(
        name="giant acid ant",
        ap_id=117,
        region="Ant Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "giant army ant": TomeEnemyLocation(
        name="giant army ant",
        ap_id=118,
        region="Ant Tier 3",
        is_boss=False,
        minimum_goal=3
    ),
    "green ooze": TomeEnemyLocation(
        name="green ooze",
        ap_id=119,
        region="Ooze Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "red ooze": TomeEnemyLocation(
        name="red ooze",
        ap_id=120,
        region="Ooze Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "blue ooze": TomeEnemyLocation(
        name="blue ooze",
        ap_id=121,
        region="Ooze Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "yellow ooze": TomeEnemyLocation(
        name="yellow ooze",
        ap_id=123,
        region="Ooze Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "white ooze": TomeEnemyLocation(
        name="white ooze",
        ap_id=122,
        region="Ooze Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "black ooze": TomeEnemyLocation(
        name="black ooze",
        ap_id=124,
        region="Ooze Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "gelatinous cube": TomeEnemyLocation(
        name="gelatinous cube",
        ap_id=125,
        region="Ooze Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "crimson ooze": TomeEnemyLocation(
        name="crimson ooze",
        ap_id=126,
        region="Ooze Tier 3",
        is_boss=False,
        minimum_goal=3
    ),
    "brittle clear ooze": TomeEnemyLocation(
        name="brittle clear ooze",
        ap_id=127,
        region="Ooze Tier 3",
        is_boss=False,
        minimum_goal=3
    ),
    "slimy ooze": TomeEnemyLocation(
        name="slimy ooze",
        ap_id=128,
        region="Ooze Tier 3",
        is_boss=False,
        minimum_goal=3
    ),
    "poison ooze": TomeEnemyLocation(
        name="poison ooze",
        ap_id=129,
        region="Ooze Tier 3",
        is_boss=False,
        minimum_goal=3
    ),
    "green jelly": TomeEnemyLocation(
        name="green jelly",
        ap_id=130,
        region="Jelly Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "red jelly": TomeEnemyLocation(
        name="red jelly",
        ap_id=131,
        region="Jelly Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "blue jelly": TomeEnemyLocation(
        name="blue jelly",
        ap_id=132,
        region="Jelly Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "white jelly": TomeEnemyLocation(
        name="white jelly",
        ap_id=133,
        region="Jelly Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "yellow jelly": TomeEnemyLocation(
        name="yellow jelly",
        ap_id=134,
        region="Jelly Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "black jelly": TomeEnemyLocation(
        name="black jelly",
        ap_id=135,
        region="Jelly Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "sandworm": TomeEnemyLocation(
        name="sandworm",
        ap_id=136,
        region="Sandworm Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "sandworm destroyer": TomeEnemyLocation(
        name="sandworm destroyer",
        ap_id=137,
        region="Sandworm Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "gigantic sandworm tunneler": TomeEnemyLocation(
        name="gigantic sandworm tunneler",
        ap_id=138,
        region="Sandworm Tier 3",
        is_boss=False,
        minimum_goal=3
    ),
    "gigantic corrosive tunneler": TomeEnemyLocation(
        name="gigantic corrosive tunneler",
        ap_id=139,
        region="Sandworm Tier 3",
        is_boss=False,
        minimum_goal=3
    ),
    "minotaur": TomeEnemyLocation(
        name="minotaur",
        ap_id=140,
        region="Minotaur Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "maulotaur": TomeEnemyLocation(
        name="maulotaur",
        ap_id=141,
        region="Minotaur Tier 3",
        is_boss=False,
        minimum_goal=3
    ),
    "drem": TomeEnemyLocation(
        name="drem",
        ap_id=142,
        region="Corrupted Horror Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "dremling": TomeEnemyLocation(
        name="dremling",
        ap_id=143,
        region="Corrupted Horror Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "drem master": TomeEnemyLocation(
        name="drem master",
        ap_id=144,
        region="Corrupted Horror Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "brecklorn": TomeEnemyLocation(
        name="brecklorn",
        ap_id=145,
        region="Corrupted Horror Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "grannor'vor": TomeEnemyLocation(
        name="grannor'vor",
        ap_id=146,
        region="Corrupted Horror Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "grannor'vin": TomeEnemyLocation(
        name="grannor'vin",
        ap_id=147,
        region="Corrupted Horror Tier 1",
        is_boss=False,
        minimum_goal=1
    ),
    "dredgling": TomeEnemyLocation(
        name="dredgling",
        ap_id=148,
        region="Temporal Horror Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "dredge": TomeEnemyLocation(
        name="dredge",
        ap_id=149,
        region="Temporal Horror Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "dredge captain": TomeEnemyLocation(
        name="dredge captain",
        ap_id=150,
        region="Temporal Horror Tier 3",
        is_boss=False,
        minimum_goal=3
    ),
    "temporal stalker": TomeEnemyLocation(
        name="temporal stalker",
        ap_id=151,
        region="Temporal Horror Tier 3",
        is_boss=False,
        minimum_goal=3
    ),
    "void horror": TomeEnemyLocation(
        name="void horror",
        ap_id=152,
        region="Temporal Horror Tier 3",
        is_boss=False,
        minimum_goal=3
    ),
    "umber hulk": TomeEnemyLocation(
        name="umber hulk",
        ap_id=153,
        region="Xorn Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "xorn": TomeEnemyLocation(
        name="xorn",
        ap_id=154,
        region="Xorn Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "xaren": TomeEnemyLocation(
        name="xaren",
        ap_id=155,
        region="Xorn Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "snow giant": TomeEnemyLocation(
        name="snow giant",
        ap_id=156,
        region="Snow Giant Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "snow giant thunderer": TomeEnemyLocation(
        name="snow giant thunderer",
        ap_id=157,
        region="Snow Giant Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "snow giant boulder thrower": TomeEnemyLocation(
        name="snow giant boulder thrower",
        ap_id=158,
        region="Snow Giant Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "cold drake hatchling": TomeEnemyLocation(
        name="cold drake hatchling",
        ap_id=159,
        region="Cold Drake Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "cold drake": TomeEnemyLocation(
        name="cold drake",
        ap_id=160,
        region="Cold Drake Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "fire drake hatchling": TomeEnemyLocation(
        name="fire drake hatchling",
        ap_id=161,
        region="Fire Drake Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "fire drake": TomeEnemyLocation(
        name="fire drake",
        ap_id=162,
        region="Fire Drake Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "Varsha the Writhing": TomeEnemyLocation(
        name="Varsha the Writhing",
        ap_id=163,
        region="Daikara",
        is_boss=True,
        minimum_goal=1
    ),
    "Rantha the Worm": TomeEnemyLocation(
        name="Rantha the Worm",
        ap_id=164,
        region="Daikara",
        is_boss=True,
        minimum_goal=1
    ),
    "Horned Horror": TomeEnemyLocation(
        name="Horned Horror",
        ap_id=165,
        region="Maze",
        is_boss=True,
        minimum_goal=1
    ),
    "Minotaur of the Labyrinth": TomeEnemyLocation(
        name="Minotaur of the Labyrinth",
        ap_id=166,
        region="Maze",
        is_boss=True,
        minimum_goal=1
    ),
    "Sandworm Queen": TomeEnemyLocation(
        name="Sandworm Queen",
        ap_id=167,
        region="Sandworm Lair",
        is_boss=True,
        minimum_goal=1
    ),
    "Shardskin": TomeEnemyLocation(
        name="Shardskin",
        ap_id=168,
        region="Old Forest",
        is_boss=True,
        minimum_goal=1
    ),
    "Wrathroot": TomeEnemyLocation(
        name="Wrathroot",
        ap_id=169,
        region="Old Forest",
        is_boss=True,
        minimum_goal=1
    ),
    "ghoul": TomeEnemyLocation(
        name="ghoul",
        ap_id=194,
        region="Ghoul Tier 1",
        is_boss=False,
        minimum_goal=2
    ),
    "ghast": TomeEnemyLocation(
        name="ghast",
        ap_id=195,
        region="Ghoul Tier 2",
        is_boss=False,
        minimum_goal=2
    ),
    "slaver": TomeEnemyLocation(
        name="slaver",
        ap_id=198,
        region="Slave Tier 2",
        is_boss=False,
        minimum_goal=2
    ),
    "enthralled slave": TomeEnemyLocation(
        name="enthralled slave",
        ap_id=199,
        region="Slave Tier 2",
        is_boss=False,
        minimum_goal=2
    ),
    "blood master": TomeEnemyLocation(
        name="blood master",
        ap_id=201,
        region="Ring of Blood",
        is_boss=True,
        minimum_goal=2
    ),
    "Subject Z": TomeEnemyLocation(
        name="Subject Z",
        ap_id=203,
        region="Halfling Ruins",
        is_boss=True,
        minimum_goal=2
    ),
    "broken golem": TomeEnemyLocation(
        name="broken golem",
        ap_id=205,
        region="Golem Tier 1",
        is_boss=False,
        minimum_goal=2
    ),
    "golem": TomeEnemyLocation(
        name="golem",
        ap_id=206,
        region="Golem Tier 2",
        is_boss=False,
        minimum_goal=2
    ),
    "water imp": TomeEnemyLocation(
        name="water imp",
        ap_id=209,
        region="Aquatic Demon Tier 2",
        is_boss=False,
        minimum_goal=2
    ),
    "luminous horror": TomeEnemyLocation(
        name="luminous horror",
        ap_id=210,
        region="Horror Tier 3",
        is_boss=False,
        minimum_goal=2
    ),
    "bloated horror": TomeEnemyLocation(
        name="bloated horror",
        ap_id=249,
        region="Horror Tier 2",
        is_boss=False,
        minimum_goal=2
    ),
    "devourer": TomeEnemyLocation(
        name="devourer",
        ap_id=212,
        region="Horror Tier 2",
        is_boss=False,
        minimum_goal=2
    ),
    "blade horror": TomeEnemyLocation(
        name="blade horror",
        ap_id=213,
        region="Horror Tier 2",
        is_boss=False,
        minimum_goal=2
    ),
    "entrenched horror": TomeEnemyLocation(
        name="entrenched horror",
        ap_id=214,
        region="Aquatic Horror Tier 2",
        is_boss=False,
        minimum_goal=2
    ),
    "swarming horror": TomeEnemyLocation(
        name="swarming horror",
        ap_id=215,
        region="Aquatic Horror Tier 2",
        is_boss=False,
        minimum_goal=2
    ),
    "ravenous horror": TomeEnemyLocation(
        name="ravenous horror",
        ap_id=216,
        region="Aquatic Horror Tier 2",
        is_boss=False,
        minimum_goal=2
    ),
    "elven cultist": TomeEnemyLocation(
        name="elven cultist",
        ap_id=220,
        region="Elven Casters Tier 3",
        is_boss=False,
        minimum_goal=2
    ),
    "elven blood mage": TomeEnemyLocation(
        name="elven blood mage",
        ap_id=221,
        region="Elven Casters Tier 3",
        is_boss=False,
        minimum_goal=2
    ),
    "elven corruptor": TomeEnemyLocation(
        name="elven corruptor",
        ap_id=222,
        region="Elven Casters Tier 3",
        is_boss=False,
        minimum_goal=2
    ),
    "faeros": TomeEnemyLocation(
        name="faeros",
        ap_id=225,
        region="Faeros Tier 3",
        is_boss=False,
        minimum_goal=2
    ),
    "greater faeros": TomeEnemyLocation(
        name="greater faeros",
        ap_id=226,
        region="Faeros Tier 3",
        is_boss=False,
        minimum_goal=2
    ),
    "gwelgoroth": TomeEnemyLocation(
        name="gwelgoroth",
        ap_id=227,
        region="Gwelgoroth Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "greater gwelgoroth": TomeEnemyLocation(
        name="greater gwelgoroth",
        ap_id=228,
        region="Gwelgoroth Tier 2",
        is_boss=False,
        minimum_goal=1
    ),
    "lesser vampire": TomeEnemyLocation(
        name="lesser vampire",
        ap_id=230,
        region="Vampire Tier 2",
        is_boss=False,
        minimum_goal=2
    ),
    "vampire": TomeEnemyLocation(
        name="vampire",
        ap_id=231,
        region="Vampire Tier 2",
        is_boss=False,
        minimum_goal=2
    ),
    "master vampire": TomeEnemyLocation(
        name="master vampire",
        ap_id=232,
        region="Vampire Tier 3",
        is_boss=False,
        minimum_goal=2
    ),
    "elder vampire": TomeEnemyLocation(
        name="elder vampire",
        ap_id=233,
        region="Vampire Tier 3",
        is_boss=False,
        minimum_goal=2
    ),
    "grave wight": TomeEnemyLocation(
        name="grave wight",
        ap_id=234,
        region="Wight Tier 3",
        is_boss=False,
        minimum_goal=2
    ),
    "barrow wight": TomeEnemyLocation(
        name="barrow wight",
        ap_id=235,
        region="Wight Tier 4",
        is_boss=False,
        minimum_goal=3
    ),
    "forest wight": TomeEnemyLocation(
        name="forest wight",
        ap_id=236,
        region="Wight Tier 2",
        is_boss=False,
        minimum_goal=2
    ),
    "Grand Corruptor": TomeEnemyLocation(
        name="Grand Corruptor",
        ap_id=242,
        region="Mark of the Spellblaze",
        is_boss=True,
        minimum_goal=2
    ),
    "Protector Myssil": TomeEnemyLocation(
        name="Protector Myssil",
        ap_id=243,
        region="Mark of the Spellblaze",
        is_boss=True,
        minimum_goal=2
    ),
    "The Master": TomeEnemyLocation(
        name="The Master",
        ap_id=244,
        region="Dreadfell",
        is_boss=True,
        minimum_goal=2
    ),
    "Weirdling Beast": TomeEnemyLocation(
        name="Weirdling Beast",
        ap_id=247,
        region="Lake of Nur",
        is_boss=True,
        minimum_goal=2
    ),
}

GENERIC_LOCATION_IDS = {
    "Trolls Tier 1 (Any)": 71,
    "Canines Tier 1 (Any)": 72,
    "Canines Tier 2 (Any)": 73,
    "Vermin Tier 1 (Any)": 74,
    "Snake Tier 1 (Any)": 75,
    "Swarm Tier 1 (Any)": 76,
    "Plant Tier 2 (Any)": 77,
    "Plant Tier 1 (Any)": 78,
    "Bear Tier 1 (Any)": 79,
    "Bear Tier 2 (Any)": 80,
    "Rodent Tier 1 (Any)": 81,
    "Aquatic Critter Tier 1 (Any)": 82,
    "Aquatic Critter Tier 2 (Any)": 83,
    "Crystal Tier 1 (Any)": 84,
    "Shivgoroth Tier 1 (Any)": 85,
    "Trollmire Boss": 86,
    "Scintillating Caves Boss": 87,
    "Norgos' Lair Boss": 88,
    "Skeletons Tier 1 (Any)": 89,
    "Skeletons Tier 2 (Any)": 90,
    "Heart of the Gloom Boss": 91,
    "Rhaloren Camp Boss": 92,
    "Kor'Pul Boss": 93,
    "Molds Tier 1 (Any)": 94,
    "Elven Warriors Tier 1 (Any)": 95,
    "Elven Warriors Tier 2 (Any)": 96,
    "Elven Casters Tier 1 (Any)": 97,
    "Ant Tier 1 (Any)": 170,
    "Ant Tier 2 (Any)": 171,
    "Ooze Tier 1 (Any)": 172,
    "Ooze Tier 2 (Any)": 173,
    "Ooze Tier 3 (Any)": 174,
    "Jelly Tier 1 (Any)": 175,
    "Sandworm Tier 1 (Any)": 176,
    "Sandworm Tier 3 (Any)": 177,
    "Minotaur Tier 2 (Any)": 178,
    "Minotaur Tier 3 (Any)": 179,
    "Corrupted Horror Tier 1 (Any)": 180,
    "Temporal Horror Tier 3 (Any)": 181,
    "Temporal Horror Tier 2 (Any)": 182,
    "Xorn Tier 2 (Any)": 183,
    "Snow Giant Tier 2 (Any)": 184,
    "Cold Drake Tier 2 (Any)": 185,
    "Fire Drake Tier 2 (Any)": 186,
    "Daikara Boss": 187,
    "Maze Boss": 188,
    "Sandworm Lair Boss": 189,
    "Old Forest Boss": 190,
    "Thieves Tier 1 (Any)": 192,
    "Thieves Tier 2 (Any)": 193,
    "Ghoul Tier 1 (Any)": 196,
    "Ghoul Tier 2 (Any)": 197,
    "Slave Tier 2 (Any)": 200,
    "Ring of Blood Boss": 202,
    "Halfling Ruins Boss": 204,
    "Golem Tier 1 (Any)": 207,
    "Golem Tier 2 (Any)": 208,
    "Aquatic Demon Tier 2 (Any)": 211,
    "Horror Tier 3 (Any)": 217,
    "Horror Tier 2 (Any)": 218,
    "Aquatic Horror Tier 2 (Any)": 219,
    "Elven Casters Tier 3 (Any)": 223,
    "Faeros Tier 3 (Any)": 224,
    "Gwelgoroth Tier 2 (Any)": 229,
    "Vampire Tier 3 (Any)": 237,
    "Vampire Tier 2 (Any)": 238,
    "Wight Tier 2 (Any)": 239,
    "Wight Tier 3 (Any)": 240,
    "Wight Tier 4 (Any)": 241,
    "Mark of the Spellblaze Boss": 245,
    "Dreadfell Boss": 246,
    "Lake of Nur Boss": 248,
}

VARIANT_ONLY_TYPES = {
    0: ["Skeletons Tier 1", "Thieves Tier 1",
        "Shivgoroth Tier 1", "Aquatic Critter Tier 1"],
    1: ["Skeletons Tier 1", "Shivgoroth Tier 1",
        "Aquatic Critter Tier 1", "Canines Tier 2",
        "Minotaur Tier 2", "Corrupted Horror Tier 1",
        "Temporal Horror Tier 2", "Cold Drake Tier 2", "Fire Drake Tier 2"],
    2: ["Shivgoroth Tier 1", "Canines Tier 2",
        "Minotaur Tier 2", "Corrupted Horror Tier 1",
        "Temporal Horror Tier 2", "Cold Drake Tier 2",
        "Fire Drake Tier 2", "Horror Tier 3",
        "Horror Tier 2", "Aquatic Horror Tier 2"],
}


def get_all_location_ids():
    all_locations = {key: value.ap_id for key, value in ENEMY_LOCATIONS.items()}
    for name, ap_id in GENERIC_LOCATION_IDS.items():
        all_locations[name] = ap_id
    return all_locations


ALL_LOCATION_IDS = get_all_location_ids()


class TOMELocation(Location):
    game = "TOME"


def create_all_locations(world: TOMEWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def should_omit_location(enemy_data, objective, require_alt_zones) -> bool:
    if enemy_data.minimum_goal > objective:
        return True
    if enemy_data.region in VARIANT_ONLY_TYPES[objective] and not require_alt_zones:
        return True
    return False

def get_location_name_for_enemy(enemy_data, merge_boss, merge_generic):
    if enemy_data.is_boss and merge_boss:
        return enemy_data.region + " Boss"
    if not enemy_data.is_boss and merge_generic:
        return enemy_data.region + " (Any)"
    return enemy_data.name

def create_regular_locations(world: TOMEWorld) -> None:
    created_locations = set()
    for _, data in ENEMY_LOCATIONS.items():
        if should_omit_location(data, world.options.objective, world.options.require_alt_zones):
            continue
        merge_bosses = not world.options.require_alt_zones
        location_name = get_location_name_for_enemy(
            data, merge_bosses, world.options.merge_generic_enemy_locations)
        if location_name not in created_locations:
            created_locations.add(location_name)
            world.get_region(data.region).add_locations(
                {location_name: ALL_LOCATION_IDS[location_name]},
                TOMELocation
            )


def create_events(world: TOMEWorld) -> None:
    if world.options.objective == 0:
        for zone in ("Trollmire", "Norgos' Lair",
                     "Scintillating Caves", "Kor'Pul",
                     "Rhaloren Camp", "Heart of the Gloom"):
            world.get_region(zone).add_event(
                f"{zone} Boss Defeated", "Tier 1 Boss",
                location_type=TOMELocation, item_type=items.TOMEItem
            )
    elif world.options.objective == 1:
        for zone in ("Maze", "Old Forest", "Sandworm Lair", "Daikara"):
            world.get_region(zone).add_event(
            f"{zone} Boss Defeated", "Tier 2 Boss",
                location_type=TOMELocation, item_type=items.TOMEItem
            )
    elif world.options.objective == 2:
        world.get_region("Dreadfell").add_event(
            "Vampire Crusher", "Vampire Crusher",
            location_type=TOMELocation, item_type=items.TOMEItem
        )
