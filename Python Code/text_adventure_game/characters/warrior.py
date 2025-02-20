# characters/warrior.py

from .character import Character  # Importing the base Character class

class Warrior(Character):
    def __init__(self, name):
        # Initialize the Warrior with a name, health, and attack power
        super().__init__(name, health=100, attack_power=20)  # Call the parent constructor

    def choose_action(self):
        # Display action options to the player
        print("\nChoose your action:")
        print("1. Attack 1 (basic attack)")  # Option for basic attack
        print("2. Attack 2 (powerstrike)")   # Option for powerstrike attack
        print("3. Defend")                   # Option to defend
        choice = input("Enter action type (1, 2, or 3): ")  # Get user input for action choice

        # Determine the action based on user input
        if choice == '1':
            return "attack1"  # Return action type for Attack 1
        elif choice == '2':
            return "attack2"  # Return action type for Attack 2
        elif choice == '3':
            return "defend"    # Return action type for Defend
        else:
            return "invalid"    # Return "invalid" for any other input