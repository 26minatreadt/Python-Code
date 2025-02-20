import random  # Import the random module to generate random actions

from characters.mage import Mage  # Import the Mage class from the mage module
from characters.warrior import Warrior  # Import the Warrior class from the warrior module

def get_random_action(character):
    actions = []  # Initialize an empty list to hold possible actions
    if isinstance(character, Mage):  # Check if the character is an instance of Mage
        actions = ['attack1', 'attack2', 'heal', 'defend']  # Define actions for Mage
    elif isinstance(character, Warrior):  # Check if the character is an instance of Warrior
        actions = ['attack1', 'attack2', 'defend']  # Define actions for Warrior
    return random.choice(actions)  # Return a random action from the list of actions