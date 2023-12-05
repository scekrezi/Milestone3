import time

def start_game():
    print("Welcome to Ravenwood!")
    time.sleep(1)
    print("You, a brave adventurer, stand in the town square, surrounded by mystical energy.")
    time.sleep(1)
    print("To open the door to the next chapter, you must solve three fun and easy riddles. Good luck!")

def riddle_1():
    print("\nRiddle 1:")
    print("I fly without wings. I cry without eyes. Wherever I go, darkness follows me. What am I?")
    answer = input("Your answer: ").lower()
    return answer == "a cloud"

def riddle_2():
    print("\nRiddle 2:")
    print("The more you take, the more you leave behind. What am I?")
    answer = input("Your answer: ").lower()
    return answer == "footsteps"

def riddle_3():
    print("\nRiddle 3:")
    print("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?")
    answer = input("Your answer: ").lower()
    return answer == "an echo"

def solve_riddles():
    print("\nTo open the door, solve these fun and easy riddles...")
    time.sleep(1)
    if riddle_1() and riddle_2() and riddle_3():
        print("\nCongratulations! The door creaks open, revealing a passage to the next chapter.")
        time.sleep(1)
        return True
    else:
        print("\nThe door remains sealed. The answers to the riddles hold the key.")
        return False

def head_to_forest():
    print("\nYou step through the open door and find yourself in the enchanted forest filled with wonders.")
    time.sleep(1)
    print("Welcome to the magical realm of Ravenwood!")

# Main game loop
start_game()

while True:
    if solve_riddles():
        head_to_forest()
        print("\nEnd Chapter 1")
        break
    else:
        retry = input("Would you like to try again? (yes/no): ").lower()
        if retry != "yes":
            print("\nYou decide to explore other parts of Ravenwood. End Chapter 1.")
            break

import time

def print_with_delay(text, delay=1):
    print(text)
    time.sleep(delay)

def start_chapter_2():
    print_with_delay("Welcome to Chapter 2 - The Enchanted Forest!")

def explore_forest():
    print_with_delay("You step into the dense atmosphere of the mysterious forest.")
    print_with_delay("The ancient trees seem to come alive with whispers, revealing the magic within.")

def investigate_cabin():
    print_with_delay("As you explore, you discover a secluded cabin.")
    return input("Would you like to investigate further and enter the cabin? (yes/no): ").lower() == 'yes'

def read_diary():
    print_with_delay("Inside the cabin, you find a dusty shelf with an old diary.")
    return input("Do you want to read the diary? (yes/no): ").lower() == 'yes'

def encounter_strange_figure():
    print_with_delay("Suddenly, a mysterious figure emerges from the shadows, revealing itself as a guardian spirit of the forest.")
    return input("Do you want to engage in conversation with the spirit or try to sneak away quietly? (talk/sneak): ").lower()

def engage_in_conversation():
    print_with_delay("You choose to engage in a conversation with the guardian spirit.")
    print_with_delay("The spirit shares ancient wisdom and tales of Ravenwood, providing guidance for your quest.")

def sneak_away():
    print_with_delay("You decide to sneak away quietly, avoiding the attention of the guardian spirit.")
    print_with_delay("Moving silently through the forest, you continue your exploration.")

def follow_footprints():
    return input("While exploring, you notice strange footprints on the forest floor. Do you want to follow them? (yes/no): ").lower() == 'yes'

def end_chapter_2():
    print_with_delay("Congratulations! You've completed Chapter 2 of your adventure in Ravenwood.")

# Main game loop for Chapter 2
start_chapter_2()
explore_forest()

if investigate_cabin():
    if read_diary():
        print_with_delay("You immerse yourself in the tales of the diary, gaining insights into Ravenwood's history.")

action = encounter_strange_figure()
if action == 'talk':
    engage_in_conversation()
else:
    sneak_away()

if follow_footprints():
    print_with_delay("You decide to follow the mysterious footprints, eager to uncover more secrets.")
    print_with_delay("Your journey continues to Chapter 3.")

end_chapter_2()
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
import Chapter3
def start_chapter_4():
    # Describe the player's arrival at the next location
    print("\nYou find and enter a hidden crypt beneath the town cemetery.")

    # Prompt the player to investigate the cult gathering place or explore the hidden passage
    player_input = input("\nDo you want to investigate the cult gathering place or explore the hidden passage? (type 'cult' or 'passage'): ")

    # If the player chooses to investigate the cult gathering place, proceed accordingly
    if player_input == "cult":
        investigate_cult_gathering_place()

    # If the player chooses to explore the hidden passage, proceed accordingly
    else:
        explore_hidden_passage()


def investigate_cult_gathering_place():
    # cult gathering place environment
    print("\nYou cautiously approach the cult gathering place, hearing strange chanting and come across a ritual.")

    # Prompt the player to hide and observe or confront the cultists
    player_input = input("\nDo you want to hide and observe or confront the cultists? (type 'hide' or 'confront'): ")

    # If the player chooses to hide and observe, proceed accordingly
    if player_input == "hide":
        hide_and_observe()

    # If the player chooses to confront the cultists, proceed accordingly
    else:
        confront_cultists()


def hide_and_observe():
    # Describe the player's attempt to hide and observe the cultists
    print("\nYou find a hiding spot and observe the cultists performing their rituals.")
    # Gather information about the cultists and their plans
    # Proceed to the next chapter
    import Chapter5


def confront_cultists():
    # Describe the player's confrontation with the cultists
    print("\nYou step out of your hiding spot and confront the cultists.")
    # The outcome of the confrontation depends on the player's choices and actions
    # Proceed to the next chapter
    import Chapter5


def explore_hidden_passage():
    # Describe the hidden passage
    print("\nYou follow the hidden passage into the darkness.")

    # Prompt the player to explore the passage or return to the crypt
    player_input = input("\nDo you want to explore the passage or return to the crypt? (type 'explore' or 'crypt'): ")

    # If the player chooses to explore the passage, proceed accordingly
    if player_input == "explore":
        explore_further()

    # If the player chooses to return to the crypt, proceed accordingly
    else:
        start_chapter_4()


def explore_further():
    # Describe the player's exploration
    print("\nYou continue exploring, but you do not find anything of interest.")

    # Prompt the player to return to the crypt
    player_input = input("\nDo you want to return to the crypt? (type 'crypt'): ")

    # If the player chooses to return to the crypt, proceed accordingly
    if player_input == "crypt":
        start_chapter_4()




# Start the game
start_chapter_4()
def start_chapter_5():
    # Describe the player's arrival at the next location
    print("You arrive at the cult leader's hidden lair.")

    # Prompt the player to confront the cult leader or take the evidence to the authorities
    player_input = input("Do you want to confront the cult leader or take the evidence to the authorities? (type 'confront' or 'authorities'): ")

    # If the player chooses to confront the cult leader, proceed accordingly
    if player_input == "confront":
        confront_cult_leader()

    # If the player chooses to take the evidence to the authorities, proceed accordingly
    else:
        take_evidence_to_authorities()

def confront_cult_leader():
    # Describe the player's confrontation with the cult leader
    print("You enter the cult leader's inner sanctum and confront them.")

    # Gather evidence during the confrontation
    evidence_gathered = gather_evidence_during_confrontation()

    # Determine the outcome based on the collected evidence and player actions
    if evidence_gathered and player_effectiveness_in_confrontation():
        print("Your bravery and quick thinking have helped you bring down the cult leader and their sinister plans.")
        good_ending()
    elif evidence_gathered:
        print("You have captured the cult leader, but without sufficient evidence to expose their plans.")
        alternate_ending()
    else:
        print("The cult leader has managed to escape your grasp, leaving you to wonder what their next move might be.")
        bad_ending()

def gather_evidence_during_confrontation():
    # the process of gathering evidence during the confrontation
    # Use player actions and clues to obtain evidence
    # Return True if evidence is gathered, False otherwise

    evidence_gathered = False  # Replace this placeholder with the actual outcome
    return evidence_gathered

def take_evidence_to_authorities():
    # Describe the player's journey to the authorities
    print("You make your way to the police station, carrying the evidence you gathered against the cult.")

    # Use the collected evidence to persuade the authorities
    evidence_persuasive = convince_authorities_with_evidence()

    # Determine the outcome based on the authorities' response
    if evidence_persuasive:
        print("The authorities have taken your evidence seriously and are preparing to take action against the cult.")
        good_ending()
    elif evidence_partially_persuasive():
        print("The authorities are somewhat convinced of the cult's threat, but need more evidence to take immediate action.")
        alternate_ending()
    else:
        print("The authorities dismissed your evidence, leaving you to deal with the cult alone.")
        bad_ending()

def convince_authorities_with_evidence():
    # the process of using evidence to persuade the authorities
    # Return True if the evidence is persuasive, False otherwise

    evidence_persuasive = True
    return evidence_persuasive

def good_ending():
    # Describe the good ending of the game
    print("You have successfully defeated the cult and saved the day. You are hailed as a hero.")

    # End the game
    quit()

def bad_ending():
    # Describe the bad ending of the game
    print("Your actions have hindered the cult's plans, but they remain at large. The threat of the cult still remains.")
    # End the game
    quit()

def alternate_ending():
    # Describe the alternate ending of the game
    print("You have made significant progress in exposing the cult, but their threat remains. You have failed.")

    # End the game
    quit()

# Start the game from Chapter 5
start_chapter_5()