"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Import the random module.

import random


# Create the start_game function.
# Write your code inside this function.

#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
#   2. Store a random number as the answer/solution.
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".

#   4. Once the guess is correct, stop looping, inform the user they "Got it"
#      and show how many attempts it took them to get the correct number.
#   5. Let the player know the game is ending, or something that indicates the game is over.

# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.
high_score = 0
def start_game():
    global high_score
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")
    print("Try to guess the number.")
    if(high_score > 0):
        print(f"The current high score is {high_score}. Good luck")
    answer = random.randint(1, 10)
    attempts = 0
    while True:
        try:
            guess = int(input("Your guess: "))
            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
                continue
            attempts += 1
            if guess < answer:
                print("It's higher")
            elif guess > answer:
                print("It's lower")
            else:
                print("Got it!")
                print(f"It took you {attempts} attempts.")
                if high_score == 0 or attempts < high_score:
                    high_score = attempts
                    print(f"Congratulations! You have the new high score: {high_score}")

                play_again = input("Would you like to play again? (yes/no) ")
                if play_again.lower() == "yes":
                    print(f"The current high score is {high_score}. Good luck")

                    answer = random.randint(1, 10)
                    attempts = 0
                    continue
                else:
                    print("Thanks for playing!")
                    break
        except ValueError:
            print("Please enter a valid number.")


start_game()