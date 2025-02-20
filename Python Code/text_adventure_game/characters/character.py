# characters/character.py

class Character:
    def __init__(self, name, health, attack_power):
        # Initialize the character with a name, health, and attack power
        self.name = name  # Character's name
        self.health = health  # Character's health points
        self.attack_power_ = attack_power  # Character's base attack power
        self.defending = False  # Indicates if the character is currently defending

    def choose_action(self):
        # This method should be overridden by subclasses to define specific actions
        raise NotImplementedError("This method should be overridden by subclasses")
    
    def attack(self, target, attack_type):
        # Determine the damage based on the attack type
        if attack_type == "attack1":
            damage = self.attack_power  # Damage for Attack 1
            print(f"{self.name} uses Attack 1!")  # Notify the action
        elif attack_type == "attack2":
            damage = self.attack_power + 5  # Increased damage for Attack 2
            print(f"{self.name} uses Attack 2!")  # Notify the action
        elif attack_type == "heal":
            damage = 0  # Healing does not deal damage
            print(f"{self.name} attempts to heal!")  # Notify the healing action
        else:
            damage = self.attack_power  # Default attack damage
            print(f"{self.name} uses a basic attack!")  # Notify the action

        # Check if the target is defending
        if target.defending:
            print(f"{target.name} defended the attack!")  # Notify that the target defended
            damage = 0  # No damage if defending
            target.defending = False  # Reset defending status
        
        target.health -= damage  # Apply damage to the target's health
        print(f"{self.name} attacks {target.name} for {damage} damage")  # Notify the damage dealt

    def defend(self):
        # Set the character to defend against the next attack
        self.defending = True  # Activate defending status
        print(f"{self.name} is defending against the next attack!")  # Notify the defending action

    def is_alive(self):
        # Check if the character's health is above zero
        return self.health > 0  # Return True if alive, False otherwise
    
    def __str__(self):
        # Return a string representation of the character's status
        return f"{self.name}: Health = {self.health}, Attack Power = {self.attack_power}"  # Status representation
