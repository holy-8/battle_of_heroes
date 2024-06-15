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

    def after_init(self):
        ...

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

    def after_init(self):
        ...

    def before_apply(self, target):
        ...

    def got_attacked(self, target, attacker, damage):
        attacker.cur_health -= 15

class Rage(Effect):
    """
    Berserk's ability: Rage effect (Buff).
    Drains 40% of target's current health, but increases its damage by the same amount.
    """
    # -- Parameters to modify -- #
    duration: int = 1
    effect_type: EffectType = EffectType.BUFF

    def after_init(self):
        ...

    def before_apply(self, target):
        health_loss = round(target.cur_health * 0.40)
        target.cur_health -= health_loss
        for key in target.cur_damage:
            target.cur_damage[key] = target.cur_damage[key] + health_loss

    def got_attacked(self, target, attacker, damage):
        ...

class DefenderProtection(Effect):
    """
    Defender's ability: Defender's protection effect (Buff).
    Defender receives damage instead of this target.
    When initializing this effect, parent should be set to defender that will receive damage.
    """
    # -- Parameters to modify -- #
    duration: int = 1
    effect_type: EffectType = EffectType.BUFF

    def after_init(self, parent):
        self.parent = parent

    def before_apply(self, target):
        ...

    def got_attacked(self, target, attacker, damage):
        target.cur_health += damage
        self.parent.cur_health -= damage
