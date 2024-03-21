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


class Wizard(Hero):
    """
    === STATS ===

    HP: 41;
    Damage: 23/12x2/7x3;
    Defense: 2.

    === ABILITY ===

    Targets: any ally or self.
    Casts "electric shield" on ally or self.
    Lasts 2 turns. Attacker receives 15 RAW damage.

    === TRAIT ===

    Can attack 1, 2 or 3 targets at the same time.
    """
    # -- Parameters to modify -- #
    max_health: int = 41
    damage: dict[int: int] = {1: 23, 2: 12, 3: 7}
    defense: int = 2
    ability_reload: int = 1
    ability_charge: int = -1

    def before_attack(self, targets: list):
        ...

    def before_defend(self):
        ...

    def before_ability(self, targets: list):
        assert len(targets) == 1
        new_effect = effects.ElectricShield()
        targets[0].cur_effects.append(new_effect)
        targets[0].cur_effects.apply_all()
