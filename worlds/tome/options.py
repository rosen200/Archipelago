from dataclasses import dataclass

from Options import Choice, PerGameCommonOptions, Range, Toggle, DefaultOnToggle, OptionSet

class MergeGenericEnemyLocations(DefaultOnToggle):
    """Combine all enemies in a given category into a single location.
    For example, instead of having separate locations for each
    different type of rodent, you'll have one location awarded for
    killing any rodent. Note that without this you will likely need
    multiple characters to find all enemies.
    """
    display_name = "Merge Generic Enemy Locations"

class RequireAllZones(Toggle):
    """Allow logic to consider zones, including alternate versions,
    mutually exclusive zones, and zones that may not appear in a given
    playthrough. If this options is turned off only enemies that
    frequently appear in both the normal and alternate versions of a
    zone will be in logic and enemies from mutually exclusive or
    non-guaranteed zones will never be in logic. Additionally the
    normal and alternate bosses as well as individual bosses of
    mutually exclusive zones will be separate locations.
    """
    display_name = "Require All Zones"

class Objective(Choice):
    """What condition should be required for goal."""
    display_name = "Objective"

    option_tier1_zones = 0
    option_into_the_darkness = 1
    option_vampire_crusher = 2
    option_tannen = 3
    option_sorcerors = 4

    default = option_tannen

class IncludeProdigy(Toggle):
    """Add a prodigy point to the item pool."""
    display_name = "Include Prodigy"

class IncludeCategoryPoint(Toggle):
    """Add a category talent point to the item pool."""
    display_name = "Include Category Point"

class NumClassPoints(Range):
    """Number of class talent points to add to the item pool."""
    display_name = "Number of Class Points"

    range_start = 0
    range_end = 3
    default = 0

class NumGenericPoints(Range):
    """Number of generic talent points to add to the item pool."""
    display_name = "Number of Generic Points"

    range_start = 0
    range_end = 3
    default = 0

class NumExtraLives(Range):
    """Number of extra lives to add to the item pool."""
    display_name = "Number of Extra Lives"

    range_start = 0
    range_end = 3
    default = 0

class NumStatPoints(Range):
    """Number of stat points to add to the item pool."""
    display_name = "Number of Stat Points"

    range_start = 0
    range_end = 10
    default = 0

class NumLevelUps(Range):
    """Number of level ups to add to the item pool."""
    display_name = "Number of Level Ups"

    range_start = 0
    range_end = 5
    default = 0

class RequiredStarts(OptionSet):
    """Race or Class specific zones that can be logically required.

    Valid values are:
     - "Yeek" (includes Murgol's Lair and Ritch Tunnels)
     - "Dwarf" (includes Escape from Reknor and Deep Bellow)
     - "Undead" (includes Blighted Ruins)
     - "Archmage" (includes Abashed Expanse)
     - "Chronomancer" (includes Unhallowed Morass)
     - "Celestial" (include Slazish Fens)
     - "Cursed" (includes Tranquil Meadow, which isn't a starting zone)
    """
    display_name = "Required Starts"

    valid_keys = frozenset({"Dwarf", "Yeek", "Undead", "Archmage",
                            "Chronomancer", "Celestial", "Cursed"})
    default = frozenset()

@dataclass
class TOMEOptions(PerGameCommonOptions):
    merge_generic_enemy_locations: MergeGenericEnemyLocations
    require_all_zones: RequireAllZones
    objective: Objective
    include_prodigy: IncludeProdigy
    include_category_point: IncludeCategoryPoint
    num_class_points: NumClassPoints
    num_generic_points: NumGenericPoints
    num_extra_lives: NumExtraLives
    num_stat_points: NumStatPoints
    num_level_ups: NumLevelUps
    required_starts: RequiredStarts
