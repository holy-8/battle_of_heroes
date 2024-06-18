from src.heroes import *

team_red = [
    Warrior(),
    Wizard(),
    Berserk()
]

team_blue = [
    Warrior(),
    Archer(),
    Necromancer()
]

team_red[0].attack(targets=[team_blue[1]])

team_blue[1].start_turn()
team_blue[1].attack(targets=[team_red[1]])

print(f'Team red: {team_red}')
print(f'Team blue: {team_blue}')
