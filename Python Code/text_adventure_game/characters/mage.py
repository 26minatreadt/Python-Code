# characters/mage.py

from .character import Character  # Importing the Character class as a base class

class Mage(Character):
    def __init__(self, name):
        # Initialize the Mage with a name, health, and attack power
        super().__init__(name, health=100, attack_power=20)  # Call the parent constructor

    def choose_action(self):
        from .actions import get_random_action  # Lazy import of the random action
        enemy_action = get_random_action(self)  # Get a random action from the enemy
        print("\nChoose your action:")  # Prompt for action choice
        print("1. Attack 1 (Fireball)")  # Option 1
        print("2. Attack 2 (Lightning Bolt)")  # Option 2
        print("3. Heal")  # Option 3
        print("4. Defend")  # Option 4
        choice = input("Enter your Action Type (1, 2, 3, or 4): ")  # Get user input for action choice

        # Determine the action based on user input
        if choice == '1':
            return "attack1"  # Return action type for Attack 1
        elif choice == '2':
            return "attack2"  # Return action type for Attack 2
        elif choice == '3':
            return "heal"  # Return action type for Heal
        elif choice == '4':
            self.defend()  # Call defend method
            return "defend"  # Return action type for Defend
        else:
            print("Invalid choice. Defaulting to Attack 1.")  # Handle invalid input
            return "attack1"  # Default action if input is invalid
        
    def heal(self):
        heal_amount = 20  # Amount of health to restore
        self.health += heal_amount  # Increase the Mage's health
        print(f"{self.name} casts Heal and restores {heal_amount} health points!")  # Notify healing action