from src.heroes import *

team_red = [
    Warrior(),
    Wizard(),
    Berserk()
]

team_blue = [
    Warrior(),
    Healer(),
    Necromancer()
]

team_red[0].attack(targets=[team_blue[1]])

team_blue[2].ability(targets=[team_blue[1]])

print(f'Team red: {team_red}')
print(f'Team blue: {team_blue}')
