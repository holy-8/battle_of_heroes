from src.heroes import Warrior, Wizard

team_red = [
    Warrior(),
    Wizard()
]

team_blue = [
    Warrior(),
    Warrior(),
    Warrior()
]

team_red[1].ability(targets=[team_red[0]])

team_blue[0].attack(targets=[team_red[0]])

print(f'Team red: {team_red}')
print(f'Team blue: {team_blue}')
