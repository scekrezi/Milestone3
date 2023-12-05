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
