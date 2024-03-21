from src._enums import EffectType
from src.base_effect import Effect


class Strength(Effect):
    """
    Warrior's ability: Strength effect (Buff).
    Multiplies target's damage by x2.25 for 1 turn.
    """
    # -- Parameters to modify -- #
    duration: int = 1
    effect_type: EffectType = EffectType.BUFF

    def before_apply(self, target):
        for key in target.cur_damage:
            target.cur_damage[key] = round(target.cur_damage[key] * 2.25)

    def got_attacked(self, target, attacker, damage):
        ...


class ElectricShield(Effect):
    """
    Wizards's ability: Electric shield effect (Buff).
    Attacker receives 15 RAW damage. Shield lasts 2 turns.
    """
    # -- Parameters to modify -- #
    duration: int = 2
    effect_type: EffectType = EffectType.BUFF

    def before_apply(self, target):
        ...

    def got_attacked(self, target, attacker, damage):
        attacker.cur_health -= 15
