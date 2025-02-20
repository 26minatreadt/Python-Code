# battles/battle.py

# Importing the Mage and Warrior classes from their respective modules
from characters.mage import Mage
from characters.warrior import Warrior
# Importing the execute_battle function from the battle_logic module
from .battle_logic import execute_battle

def battle(player, enemy):
    # Call the execute_battle function to initiate the battle between the player and the enemy
    # player: the character controlled by the user
    # enemy: the character controlled by the AI
    execute_battle(player, enemy)