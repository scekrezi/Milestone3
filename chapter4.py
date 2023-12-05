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