from dataclasses import dataclass

from Options import Choice, PerGameCommonOptions, Range, Toggle

class MergeGenericEnemyLocations(Toggle):
    """Combine all enemies in a given category into a single location.
    For example, instead of having separate locations for each
    different type of rodent, you'll have one location awarded for
    killing any rodent."""
    display_name = "Merge Generic Enemy Locations"

class RequireAltZones(Toggle):
    """Allow logic to consider both the normal and alternate versions
    of early zones. If this options is turned off only enemies that
    frequently appear in both the normal and alternate versions of a
    zone will be in logic. Additionally the normal and alternate
    bosses will be separate locations.
    """
    display_name = "Require Alt Zones"

class Objective(Choice):
    display_name = "Objective"

    option_tier1_zones = 0
    option_into_the_darkness = 1
    option_vampire_crusher = 2

    default = option_tier1_zones

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

@dataclass
class TOMEOptions(PerGameCommonOptions):
    merge_generic_enemy_locations: MergeGenericEnemyLocations
    require_alt_zones: RequireAltZones
    objective: Objective
    include_prodigy: IncludeProdigy
    include_category_point: IncludeCategoryPoint
    num_class_points: NumClassPoints
    num_generic_points: NumGenericPoints
    num_extra_lives: NumExtraLives
    num_stat_points: NumStatPoints
