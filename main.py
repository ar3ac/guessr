import random
from view import display_welcome_message


def main():
    number_to_guess = random.randint(1, 100)
    display_welcome_message()
    difficulty = input("Select difficulty level (1, 2, or 3): ")
    if difficulty not in ["1", "2", "3"]:
        print("Invalid selection. Please select 1, 2, or 3.")
        return

    level_map = {"1": 10, "2": 5, "3": 3}
    max_attempts = level_map[difficulty]

    print(f"You selected difficulty level {difficulty}.")

    while max_attempts > 0:
        print(f"You have {max_attempts} attempts.")

        guess_input = input("Enter your guess: ")

        if not guess_input.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        guess = int(guess_input)

        if not (1 <= guess <= 100):
            print("Please enter a number between 1 and 100.")
            continue

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number!")
            break

        max_attempts -= 1
        # print(f"You guessed: {guess}")  # Placeholder per le prossime fasi
        # break  # Interrompiamo temporaneamente per evitare loop infiniti
    else:  # Questo blocco viene eseguito solo se il ciclo while finisce senza un 'break'
        print("\nThe attempts are over!")
        print(f"The number to guess was: {number_to_guess}")


if __name__ == "__main__":
    main()
