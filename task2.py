import time

def intro():
    print("Welcome to the Text Adventure Game!")
    time.sleep(2)
    print("You find yourself in a mysterious forest.")
    time.sleep(2)
    print("Your goal is to reach the end of the forest and discover its secrets.")
    time.sleep(2)
    print("Be careful with your choices; they will determine your fate!")

def make_choice(choices):
    print("\nChoose your action:")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    while True:
        try:
            choice_num = int(input("Enter the number of your choice: "))
            if 1 <= choice_num <= len(choices):
                return choice_num
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def forest_path():
    print("\nYou start walking on a path through the dense forest.")
    time.sleep(2)
    print("You hear strange noises in the bushes.")
    time.sleep(2)

    choices = ["Investigate the noises.", "Ignore the noises and continue walking."]
    choice = make_choice(choices)

    if choice == 1:
        print("\nYou cautiously approach the source of the noise.")
        time.sleep(2)
        print("You discover a friendly creature that offers you a magical amulet.")
        inventory.append("Magical Amulet")
        print("You add the Magical Amulet to your inventory.")
        time.sleep(2)
        print("You continue on the path.")
    else:
        print("\nYou decide to ignore the noises and keep walking.")

def encounter_enemy():
    print("\nAs you proceed, you encounter a fearsome enemy blocking your way.")
    time.sleep(2)

    if "Sword" in inventory:
        print("You draw your sword and prepare for battle.")

        choices = ["Fight the enemy.", "Try to sneak around."]
        choice = make_choice(choices)

        if choice == 1:
            print("\nYou engage in a fierce battle with the enemy.")
            time.sleep(2)
            print("With your trusty sword, you defeat the enemy.")
        else:
            print("\nYou attempt to sneak around the enemy.")
            time.sleep(2)
            print("You manage to sneak past without alerting the enemy.")
    else:
        print("You don't have any weapon to defend yourself.")

        choices = ["Try to reason with the enemy.", "Run away."]
        choice = make_choice(choices)

        if choice == 1:
            print("\nYou try to communicate with the enemy, but it attacks you.")
            time.sleep(2)
            print("You manage to escape, but you are injured.")
        else:
            print("\nYou decide to run away from the enemy.")
            time.sleep(2)
            print("You run as fast as you can and escape from the enemy.")

def reach_end():
    print("\nAfter overcoming various challenges, you reach the end of the forest.")
    time.sleep(2)

    if "Magical Amulet" in inventory:
        print("The magical amulet you found earlier starts glowing.")
        time.sleep(2)
        print("The secrets of the forest are revealed to you.")
        time.sleep(2)
        print("Congratulations! You have successfully completed the adventure.")
        time.sleep(2)
        print("Thank you for playing!")
    else:
        print("Unfortunately, you reach the end without discovering the forest's secrets.")
        time.sleep(2)
        print("Better luck next time!")

def play_game():
    intro()
    forest_path()
    encounter_enemy()
    reach_end()

# Main game loop
while True:
    inventory = []  # Reset inventory for each playthrough
    play_game()

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thank you for playing! Goodbye.")
        break
