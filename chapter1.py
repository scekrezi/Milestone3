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
