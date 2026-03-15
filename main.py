import random
from view import display_welcome_message


def get_user_guess():
    guess_input = input("Enter your guess: ")
    if not guess_input.isdigit():
        print("Invalid input. Please enter a number.")
        return None
    return int(guess_input)


def choose_difficulty():
    while True:
        difficulty = input("Select difficulty level (1, 2, or 3): ")
        if difficulty in ["1", "2", "3"]:
            return difficulty
        print("Invalid selection. Please select 1, 2, or 3.")


def play_round():
    """Plays a single round of the number guessing game."""
    number_to_guess = random.randint(1, 100)
    difficulty = choose_difficulty()

    level_map = {"1": 10, "2": 5, "3": 3}
    initial_attempts = level_map[difficulty]
    max_attempts = initial_attempts

    print(f"You selected difficulty level {difficulty}.")

    while max_attempts > 0:
        print(f"You have {max_attempts} attempts.")

        guess = get_user_guess()
        if guess is None:
            continue

        if not (1 <= guess <= 100):
            print("Please enter a number between 1 and 100.")
            continue

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            used_attempts = initial_attempts - max_attempts + 1
            print(
                f"Congratulations! You guessed the number in {used_attempts} attempts."
            )
            return  # Esce dalla funzione play_round dopo la vittoria

        max_attempts -= 1

    # Questo codice viene raggiunto solo se il ciclo while termina (sconfitta)
    print("\nThe attempts are over!")
    print(f"The number to guess was: {number_to_guess}")


def main():
    """Main function to control the game flow."""
    display_welcome_message()
    while True:
        play_round()

        while True:
            play_again = input("\nDo you want to play again? (y/n): ").lower()
            if play_again in ["y", "yes"]:
                break  # Esce dal loop interno, ricomincia il loop esterno (nuova partita)
            elif play_again in ["n", "no"]:
                print("Thanks for playing! Goodbye!")
                return  # Esce dalla funzione main, chiudendo il programma
            else:
                print("Invalid input. Please type 'y' or 'n'.")


if __name__ == "__main__":
    main()
