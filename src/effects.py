from _enums import EffectType
from base_effect import Effect


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
