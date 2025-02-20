import random  # Import the random module to generate random numbers

def player_attack(player):
    # Prompt the player to choose an attack option
    player_action = input("Choose your attack (1 or 2):")
    # Check if the player's choice is valid (either '1' or '2')
    if player_action not in ['1', '2']:
        print("Invalid choice. Defaulting to Attack 1.")  # Inform the player of the invalid choice
        player_action = '1'  # Default to Attack 1 if the choice is invalid
    return player_action  # Return the player's chosen attack

def enemy_defend():
    # Generate a random defense choice for the enemy (either '1' or '2')
    return str(random.randint(1, 2))  # Return the random defense as a string

def player_defend():
    # Prompt the player to choose a defense option
    player_defense = input("Choose your defense (1 or 2):")
    # Check if the player's choice is valid (either '1' or '2')
    if player_defense not in ['1', '2']:
        print("Invalid choice. Defaulting to Defense 1.")  # Inform the player of the invalid choice
        player_defense = '1'  # Default to Defense 1 if the choice is invalid
    return player_defense  # Return the player's chosen defense

def enemy_attack(enemy):
    # Generate a random attack choice for the enemy (either '1' or '2')
    return str(random.randint(1, 2))  # Return the random attack as a string