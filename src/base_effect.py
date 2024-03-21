from abc import ABC, abstractmethod
from _enums import EffectType


class Effect(ABC):
    # -- Current status -- #
    is_applied: bool  # True if this effect was already applied this move.
    cur_duration: int  # Current amount of moves before this effect gets deleted, can be inf.
    # -- Parameters to modify -- #
    duration: int  # Initial amount of moves before this effect gets deleted, can be inf.
    effect_type: EffectType

    def __init__(self):
        self.name = self.__class__.__name__
        self.is_applied = False
        self.cur_duration = self.duration

    def apply(self, target):
        self.before_apply(target)
        self.is_applied = True
        self.cur_duration -= 1

    @abstractmethod
    def before_apply(self, target):
        ...


class EffectList:
    def __init__(self, parent):
        self.parent = parent
        self.effects = list()

    def append(self, new_effect: Effect):
        for index, effect in enumerate(self.effects):
            if effect.name == new_effect.name:
                self.effects.pop(index)
                break
        self.effects.append(new_effect)

    def apply_all(self):
        new_effect_list = self.effects.copy()
        for index, effect in enumerate(self.effects):
            if effect.is_applied:
                continue
            if effect.duration <= 0:
                new_effect_list.pop(index)
                continue
            new_effect_list[index].apply(target=self.parent)
        self.effects = new_effect_list

    def update_all(self):
        for effect in self.effects:
            effect.is_applied = False
