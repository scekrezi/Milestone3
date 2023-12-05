def start_chapter_3():
    # Describe the player's arrival at the next location
    print("\nFootprints lead to abandoned underground chamber.")

    # Prompt the player to explore chamber and find cryptic symbols
    player_input = input("\nDo you want to stay in chamber or explore chamber and find cryptic symbols? (type 'stay' or 'explore'): ")

    # If the player chooses to stay, proceed to the city gates
    if player_input == "stay":
        stays_chamber()
        print("\nYou chose to stay. Please restart Chapter 3.")
        start_chapter_3()  # Restart Chapter 3

    # If the player chooses to explore the chamber, proceed to explore the chamber
    else:
        explore_chamber()


def stays_chamber():
    # Describe the approach to the city gates
    print("\nYou didn’t find nothing. Try again")


def explore_chamber():
    # Describe the dimly lit chamber environment
    print("\nYou cautiously enter the chamber.")

    # Prompt the player to examine the cryptic symbols
    player_input = input("\nDo you want to examine the cryptic symbols? (type 'yes' or 'no'): ")

    # If the player chooses to examine the cryptic symbols, proceed accordingly
    if player_input == "yes":
        examine_cryptic_symbols()

    # If the player chooses not to examine the cryptic symbols, return to the previous choice
    else:
        start_chapter_3()


def examine_cryptic_symbols():
    # Describe the cryptic symbols
    print("\nYou carefully examine the cryptic symbols etched on the wall.")

    # Prompt the player to decipher the symbols
    player_input = input("\nDo you want to try to decipher the symbols? (type 'yes' or 'no'): ")

    # If the player chooses to decipher the symbols, proceed accordingly
    if player_input == "yes":
        decipher_cryptic_symbols()

    # If the player chooses not to decipher the symbols, return to the previous choice
    else:
        start_chapter_3()


def decipher_cryptic_symbols():
    # Describe the process of deciphering the cryptic symbols
    print("\nYou attempt to decipher the cryptic symbols, and you successfully uncover the location of a hidden passage.")

    # Prompt the player to continue exploring or return to the previous choice
    player_input = input("\nDo you want to explore the hidden passage or return to the previous choice? (type 'explore' or 'back'): ")

    # If the player chooses to explore the hidden passage, proceed to Chapter 4
    if player_input == "explore":
        start_chapter_4()

        # If the player chooses to return to the previous choice, redirect to the previous decision point
    elif player_input == "back":
        explore_chamber()  # Redirect to the previous decision point
    else:
        print("Invalid choice. Please enter 'explore' or 'back'.")

def start_chapter_4():
    # Describe the player's arrival in the hidden passage
    print("\nThe hidden passage leads you deeper into the maze-like tunnel.")

    # Describe the cave
    print("\nThe tunnel is dark, ... but there's light ahead.")

    # Prompt the player to venture deeper into the cavern or retrace their steps
    player_input = input("\nDo you choose to: 1. Venture deeper into the tunnel 2. Retrace your steps (type 'venture' or 'back'): ")

    # If the player chooses to venture deeper, proceed to the next chapter
    if player_input == "venture":
        # Start Chapter 4
        import Chapter4

    # If the player chooses to retrace their steps, return to the previous choice
    else:
        start_chapter_3()

start_chapter_3()
