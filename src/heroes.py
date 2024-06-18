import src.effects as effects
from src.base_hero import Hero
from math import inf


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

    def after_start_turn(self):
        ...

    def before_attack(self, targets: list):
        ...

    def before_defend(self):
        ...

    def before_ability(self, targets: list):
        assert len(targets) == 1
        assert targets[0].cur_health > 0
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

    def after_start_turn(self):
        ...

    def before_attack(self, targets: list):
        ...

    def before_defend(self):
        ...

    def before_ability(self, targets: list):
        assert len(targets) == 1
        assert targets[0].cur_health > 0
        new_effect = effects.ElectricShield()
        targets[0].cur_effects.append(new_effect)
        targets[0].cur_effects.apply_all()


class Healer(Hero):
    """
    === STATS ===

    HP: 35;
    Damage: 6;
    Defense: 3.

    === ABILITY ===

    Targets: any ally or self.
    Heals target for 25 health. Ability recharges 2 turns.

    === TRAIT ===

    None.
    """
    # -- Parameters to modify -- #
    max_health: int = 35
    damage: dict[int: int] = {1: 6}
    defense: int = 3
    ability_reload: int = 2
    ability_charge: int = -1

    def after_start_turn(self):
        ...

    def before_attack(self, targets: list):
        ...

    def before_defend(self):
        ...

    def before_ability(self, targets: list):
        assert len(targets) == 1
        assert targets[0].cur_health > 0
        targets[0].cur_health += 25


class Berserk(Hero):
    """
    === STATS ===

    HP: 62;
    Damage: 28;
    Defense: 5.

    === ABILITY ===

    Targets: any ally or self.
    Drains 40% of target's current health. Damage is increased by lost health for 1 turn.
    If used on self, damage is increased for the next turn.

    === TRAIT ===

    None.
    """
    # -- Parameters to modify -- #
    max_health: int = 62
    damage: dict[int: int] = {1: 28}
    defense: int = 5
    ability_reload: int = 1
    ability_charge: int = -1

    def after_start_turn(self):
        ...

    def before_attack(self, targets: list):
        ...

    def before_defend(self):
        ...

    def before_ability(self, targets: list):
        assert len(targets) == 1
        assert targets[0].cur_health > 0
        new_effect = effects.Rage()
        if targets[0].name == self.name:
            new_effect.cur_duration += 1
        targets[0].cur_effects.append(new_effect)
        targets[0].cur_effects.apply_all()


class Defender(Hero):
    """
    === STATS ===

    HP: 223;
    Damage: 9;
    Defense: 32.

    === ABILITY ===

    Targets: any ally.
    Defender receives damage instead of a chosen ally. Lasts 1 turn.

    === TRAIT ===

    Damage is doubled if defender's health is below 25% (less than 56 health).
    """
    # -- Parameters to modify -- #
    max_health: int = 223
    damage: dict[int: int] = {1: 9}
    defense: int = 32
    ability_reload: int = 1
    ability_charge: int = -1

    def after_start_turn(self):
        if self.cur_health < round(self.max_health * 0.25):
            self.cur_damage[1] *= 2

    def before_attack(self, targets: list):
        ...

    def before_defend(self):
        ...

    def before_ability(self, targets: list):
        assert len(targets) == 1
        assert targets[0].name != self.name
        assert targets[0].cur_health > 0
        new_effect = effects.DefenderProtection(parent=self)
        targets[0].cur_effects.append(new_effect)
        targets[0].cur_effects.apply_all()


class Necromancer(Hero):
    """
    === STATS ===

    HP: 80;
    Damage: 12;
    Defense: 7.

    === ABILITY ===

    Targets: any ally.
    Revives a dead ally. Can only be used once per battle.

    === TRAIT ===

    None.
    """
    # -- Parameters to modify -- #
    max_health: int = 80
    damage: dict[int: int] = {1: 12}
    defense: int = 7
    ability_reload: int = inf
    ability_charge: int = -1

    def after_start_turn(self):
        ...

    def before_attack(self, targets: list):
        ...

    def before_defend(self):
        ...

    def before_ability(self, targets: list):
        assert len(targets) == 1
        assert targets[0].cur_health == 0
        targets[0].cur_effects.clear_all()
        targets[0].cur_health = targets[0].max_health


class Archer(Hero):
    """
    === STATS ===

    HP: 56;
    Damage: 21;
    Defense: 10.

    === ABILITY ===

    None.

    === TRAIT ===

    Archer gains 1 extra damage for each lost hp, and vice versa.
    """
    # -- Parameters to modify -- #
    max_health: int = 56
    damage: dict[int: int] = {1: 21}
    defense: int = 10
    ability_reload: int = -1
    ability_charge: int = -1

    def after_start_turn(self):
        self.cur_damage[1] += self.max_health - self.cur_health

    def before_attack(self, targets: list):
        ...

    def before_defend(self):
        ...

    def before_ability(self, targets: list):
        assert False
