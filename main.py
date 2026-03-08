import random  # Needed for random attack damage and heal amounts

# ------------------------------
# Base Character Class
# ------------------------------
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health

    # Normal attack with randomized damage
    def attack(self, opponent):
        damage = random.randint(int(self.attack_power * 0.8), int(self.attack_power * 1.2))
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    # Heal method
    def heal(self):
        heal_amount = random.randint(15, 30)
        self.health = min(self.max_health, self.health + heal_amount)
        print(f"{self.name} heals for {heal_amount}. Current health: {self.health}/{self.max_health}")

    # Display stats
    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")


# ------------------------------
# Character Classes
# ------------------------------
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30)
        self.evade_next = False  # Track if Archer will evade next attack

    # Unique ability: Quick Shot (double attack)
    def quick_shot(self, opponent):
        damage1 = random.randint(int(self.attack_power * 0.8), int(self.attack_power * 1.2))
        damage2 = random.randint(int(self.attack_power * 0.8), int(self.attack_power * 1.2))
        total_damage = damage1 + damage2
        opponent.health -= total_damage
        print(f"{self.name} uses Quick Shot on {opponent.name} for {damage1} + {damage2} = {total_damage} damage!")

    # Unique ability: Evade
    def evade(self):
        self.evade_next = True
        print(f"{self.name} prepares to evade the next attack!")


class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=20)
        self.shield_next = False  # Track if Paladin will block next attack

    # Unique ability: Holy Strike (bonus damage)
    def holy_strike(self, opponent):
        bonus_damage = random.randint(10, 20)
        total_damage = self.attack_power + bonus_damage
        opponent.health -= total_damage
        print(f"{self.name} uses Holy Strike on {opponent.name} for {total_damage} damage!")

    # Unique ability: Divine Shield
    def divine_shield(self):
        self.shield_next = True
        print(f"{self.name} raises Divine Shield to block the next attack!")


# ------------------------------
# Evil Wizard Class
# ------------------------------
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    # Wizard regenerates health
    def regenerate(self):
        self.health += 5
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")


# ------------------------------
# Character Creation
# ------------------------------
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)


# ------------------------------
# Battle System
# ------------------------------

import time  # For small pauses

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n" + "-"*30)
        print(f"Your Health: {player.health}/{player.max_health} | Wizard Health: {wizard.health}/{wizard.max_health}")
        print("-"*30)

        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        # ----------------------
        # Player Actions
        # ----------------------
        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Warrior):
                print("Warrior has no special abilities yet. Using normal attack.")
                player.attack(wizard)
            elif isinstance(player, Mage):
                damage = random.randint(player.attack_power, player.attack_power + 10)
                wizard.health -= damage
                print(f"{player.name} casts Fireball on {wizard.name} for {damage} damage!")
            elif isinstance(player, Archer):
                print("Choose Archer ability:")
                print("1. Quick Shot")
                print("2. Evade")
                ability = input("Enter ability number: ")
                if ability == '1':
                    player.quick_shot(wizard)
                elif ability == '2':
                    player.evade()
                else:
                    print("Invalid ability. Skipping turn.")
            elif isinstance(player, Paladin):
                print("Choose Paladin ability:")
                print("1. Holy Strike")
                print("2. Divine Shield")
                ability = input("Enter ability number: ")
                if ability == '1':
                    player.holy_strike(wizard)
                elif ability == '2':
                    player.divine_shield()
                else:
                    print("Invalid ability. Skipping turn.")
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        time.sleep(1)  # Small pause for readability

        # ----------------------
        # Wizard Turn
        # ----------------------
        if wizard.health > 0:
            print("\n--- Wizard's Turn ---")
            wizard.regenerate()
            time.sleep(1)

            # Handle defensive mechanics
            if isinstance(player, Archer) and player.evade_next:
                print(f"{player.name} evades {wizard.name}'s attack!")
                player.evade_next = False
            elif isinstance(player, Paladin) and player.shield_next:
                print(f"{player.name} blocks {wizard.name}'s attack with Divine Shield!")
                player.shield_next = False
            else:
                wizard.attack(player)

        # ----------------------
        # Check for defeat
        # ----------------------
        if player.health <= 0:
            print(f"{player.name} has been defeated by {wizard.name}!")
            break
        elif wizard.health <= 0:
            print(f"{player.name} has defeated {wizard.name}! Victory!")
            break

        time.sleep(1)  # Pause between turns

    # ----------------------
    # End Game Messages
    # ----------------------
    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")
    elif player.health <= 0:
        print(f"{player.name} was defeated by {wizard.name}. Better luck next time!")


# ------------------------------
# Main Program
# ------------------------------
def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)


if __name__ == "__main__":
    main()