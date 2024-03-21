from heroes import Warrior

warrior_a = Warrior()
warrior_b = Warrior()

warrior_a.ability(targets=[warrior_a])
warrior_a.attack(targets=[warrior_b])
print(warrior_a, warrior_b)
