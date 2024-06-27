# Number Guessing Game

## Project Description
This is a simple Number Guessing Game implemented in Python. It's part of the Python Development Techdegree, Project 1. The game generates a random number between 1 and 10, and the player tries to guess it with as few attempts as possible.

## Features
- Randomly generates a number between 1 and 10 for each game
- Tracks the number of attempts for each game
- Provides hints ("It's higher" or "It's lower") based on the player's guess
- Keeps track of the high score (lowest number of attempts)
- Allows the player to play multiple games
- Handles invalid inputs gracefully

## How to Play
1. Run the script
2. The game will prompt you to guess a number between 1 and 10
3. Enter your guess
4. The game will tell you if your guess is too high or too low
5. Keep guessing until you get the correct number
6. After guessing correctly, you'll see how many attempts it took
7. You'll be asked if you want to play again
8. If you play multiple games, try to beat the high score!

## Requirements
- Python 3.x

## How to Run
1. Ensure you have Python installed on your system
2. Download the script file
3. Open a terminal or command prompt
4. Navigate to the directory containing the script
5. Run the command: `python guessing_game.py`

## Code Structure
- The game logic is encapsulated in the `start_game()` function
- The script uses a global variable `high_score` to keep track of the best score across multiple games
- Random number generation is handled by the `random` module
- Input validation ensures that only valid numbers between 1 and 10 are accepted

## Future Enhancements
- Add difficulty levels (e.g., larger number ranges)
- Implement a graphical user interface
- Add a time limit for each guess
- Store high scores persistently (e.g., in a file or database)

## Author
Adeyinka Giwa
