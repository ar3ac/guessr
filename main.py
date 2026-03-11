import random
from view import display_welcome_message


def main():
    display_welcome_message()
    difficulty = input("Select difficulty level (1, 2, or 3): ")
    print(f"You selected difficulty level {difficulty}. Let's start the game!")


if __name__ == "__main__":
    main()
