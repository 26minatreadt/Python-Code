# battle/battle_logic.py

# Importing necessary functions for player and enemy actions
from .battle_actions import player_attack, enemy_defend, player_defend, enemy_attack

def execute_battle(player, enemy):
    # Print the start of the battle with player and enemy names
    print(f"\nBattle Start: {player.name} vs {enemy.name}\n")
    print(player)  # Display player's status
    print(enemy)  # Display enemy's status
    print("-----------------------")

    turn = 1  # Initialize turn counter
    # Loop until either player or enemy is defeated
    while player.is_alive() and enemy.is_alive():
        print(f"Turn {turn}")  # Indicate the current turn

        # Prompt the player to choose an action
        action_choice = input("Choose your action (1: Attack, 2: Defend): ")
        if action_choice == '1':  # Player chooses to attack
            player_action = player_attack(player)  # Get player's attack choice
            enemy_action = enemy_defend()  # Get enemy's defense choice
            print(f"{enemy.name} chooses to defend with option {enemy_action}.")

            # Check if both actions match
            if player_action == enemy_action:
                print("No Damage dealt! Both actions matched.")  # No damage if actions match
            else:
                damage = player.attack(enemy, player_action)  # Calculate damage dealt
                print(f"{player.name} attacks {enemy.name} for {damage} damage.")  # Notify damage dealt

        elif action_choice == '2':  # Player chooses to defend
            player_defense = player_defend()  # Get player's defense choice
            enemy_action = enemy_attack(enemy)  # Get enemy's attack choice
            print(f"{enemy.name} chooses to attack with option {enemy_action}.")

            # Check if both actions match
            if player_defense == enemy_action:
                print("No Damage dealt! Both actions matched.")  # No damage if actions match
            else:
                damage = enemy.attack(player, enemy_action)  # Calculate damage dealt
                print(f"{enemy.name} attacks {player.name} for {damage} damage.")  # Notify damage dealt

        # Check if the enemy has been defeated
        if not enemy.is_alive():
            print(f"\n{enemy.name} has been defeated! {player.name} wins!")  # Notify player victory
            break  # Exit the loop

        # Check if the player has been defeated
        if not player.is_alive():
            print(f"\n{player.name} has been defeated! {enemy.name} wins!")  # Notify enemy victory
            break  # Exit the loop

        print("---------------------------")  # Separator for turns
        turn += 1  # Increment turn counter

    print("Battle is now over!")  # Notify that the battle has ended
