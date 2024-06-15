from abc import ABC, abstractmethod
from src._functions import clamp
from src.base_effect import EffectList


class Hero(ABC):
    """
    Base class for a Hero.

    === ATTRIBUTES TO MODIFY ===

    - int max_health
    - dict[int:int] damage
    - int defense
    - int ability_reload
    - int ability_charge

    === ABSTRACT METHODS ===

    - def before_attack(self, targets: list)
    - def before_defend(self)
    - def before_ability(self, targets: list)
    """
    # -- Current status -- #
    cur_health: int
    cur_damage: dict[int: int]
    cur_defense: int
    cur_effects: EffectList
    cur_ability_reload: float  # Progress from 0 to 1.
    cur_ability_charge: float  # Progress from 0 to 1.
    has_moved: bool  # True if this hero cannot move.
    # -- Parameters to modify -- #
    max_health: int
    damage: dict[int: int]  # Key - amount of targets; Value - damage dealt to that amount of targets.
    defense: int
    ability_reload: int  # How long does it take to use the ability again, in moves; Set to -1 if no ability.
    ability_charge: int  # How hong does it take to charge up the ability, in moves; Set to -1 if no charge.

    def __init__(self):
        self.name = self.__class__.__name__
        self.cur_health = self.max_health
        self.cur_damage = self.damage
        self.cur_defense = 0
        self.cur_effects = EffectList(parent=self)
        self.cur_ability_reload = 1.0
        self.cur_ability_charge = 0.0
        self.has_moved = False

    def __repr__(self):
        return f'{self.name} ({self.cur_health}/{self.max_health})'

    def __setattr__(self, key, value):
        if key == 'cur_health':
            self.__dict__[key] = clamp(value, 0, self.max_health)
        elif key in ('cur_ability_reload', 'cur_ability_charge'):
            self.__dict__[key] = clamp(value, 0.0, 1.0)
        else:
            self.__dict__[key] = value

    def start_turn(self):
        self.has_moved = False
        self.cur_damage = self.damage
        self.cur_defense = 0
        self.cur_effects.update_all()
        self.cur_effects.apply_all()
        if self.cur_ability_reload < 1:
            self.cur_ability_reload += 1 / self.ability_reload
        self.after_start_turn()

    def attack(self, targets: list):
        assert len(targets) in self.damage
        self.before_attack(targets)
        for target in targets:
            damage = self.cur_damage[len(targets)]
            target.cur_health -= damage
            target.cur_effects.got_attacked(target=target, attacker=self, damage=damage)
        self.has_moved = True

    def defend(self):
        self.before_defend()
        self.cur_defense += self.defense
        self.has_moved = True

    def ability(self, targets: list):
        self.before_ability(targets)
        self.has_moved = True
        self.cur_ability_reload = 0.0

    @abstractmethod
    def after_start_turn(self):
        ...

    @abstractmethod
    def before_attack(self, targets: list):
        ...

    @abstractmethod
    def before_defend(self):
        ...

    @abstractmethod
    def before_ability(self, targets: list):
        ...
