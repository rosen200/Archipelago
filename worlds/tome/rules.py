from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import Has

if TYPE_CHECKING:
    from .world import TOMEWorld



def set_all_rules(world: TOMEWorld) -> None:
    set_completion_condition(world)


def set_completion_condition(world: TOMEWorld) -> None:
    if world.options.objective == 0:
        world.set_completion_rule(Has("Tier 1 Boss", count=6))
    if world.options.objective == 1:
        world.set_completion_rule(Has("Tier 2 Boss", count=4))
    if world.options.objective == 2:
        world.set_completion_rule(Has("Vampire Crusher"))
    if world.options.objective == 3:
        world.set_completion_rule(Has("Tannen Defeated"))
    if world.options.objective == 4:
        world.set_completion_rule(Has("Sorcerors Defeated"))
