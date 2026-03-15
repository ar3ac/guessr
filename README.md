# guessr - a number Guessing Game

A classic command-line Number Guessing Game built with Python. The computer selects a random number between 1 and 100, and your goal is to guess it within a limited number of attempts based on the chosen difficulty level.

More accurate than a crystal ball, equally useless in real life.
( a roadmap project : https://roadmap.sh/projects/number-guessing-game )

## Features

- **3 Difficulty Levels**:
  - Easy: 10 attempts
  - Medium: 5 attempts
  - Hard: 3 attempts
- **Input Validation**: Handles non-numeric inputs and numbers out of range gracefully.
- **Replayability**: Play as many rounds as you like without restarting the script.
- **Clean Interface**: Clear feedback messages (Too high / Too low).

## How to Run

Ensure you have Python installed on your machine.

1. Clone the repository or download the files.
2. Navigate to the project directory in your terminal.
3. Run the game:

```bash
python main.py
```

## Example Session

```text
Welcome to the Number Guessing Game!

I'm thinking of a number between 1 and 100.
Please select the difficulty level:

1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Select difficulty level (1, 2, or 3): 3
You selected difficulty level 3.
You have 3 attempts.
Enter your guess: 50
Too low! Try again.
You have 2 attempts.
Enter your guess: 75
Too high! Try again.
You have 1 attempts.
Enter your guess: 60
Congratulations! You guessed the number in 3 attempts.

Do you want to play again? (y/n): n
Thanks for playing! Goodbye!
```
