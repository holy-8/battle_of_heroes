import src.effects as effects
from src.base_hero import Hero


class Warrior(Hero):
    """
    === STATS ===

    HP: 115;
    Damage: 18;
    Defense: 9.

    === ABILITY ===

    Targets: any ally or self.
    Increases attack damage by x2.25 for 1 turn.
    If used on self, damage is increased for the next turn.

    === TRAIT ===

    None.
    """
    # -- Parameters to modify -- #
    max_health: int = 115
    damage: dict[int: int] = {1: 18}
    defense: int = 9
    ability_reload: int = 1
    ability_charge: int = -1

    def before_attack(self, targets: list):
        ...

    def before_defend(self):
        ...

    def before_ability(self, targets: list):
        assert len(targets) == 1
        new_effect = effects.Strength()
        if targets[0].name == self.name:
            new_effect.cur_duration += 1
        targets[0].cur_effects.append(new_effect)
        targets[0].cur_effects.apply_all()
