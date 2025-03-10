# Number guessing game
from random import randint

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def number_guessing_game():
    print("* Welcome To Number Guessing Game *\n")
    print("I've thought of number between 1 and 100.")
    print("It's your task to make a correct guess of that number.\n")

    # attempts_remaining = 0
    difficulty = input("Choose difficulty [EASY/HARD]:\n")
    if difficulty == "easy":
        attempts_remaining = EASY_ATTEMPTS
    elif difficulty == "hard":
        attempts_remaining = HARD_ATTEMPTS
    print(f"You've {attempts_remaining} attempts remaining")

    continue_game = True
    secret_number = randint(1, 101)
    print(secret_number)
    while continue_game and attempts_remaining:
        user_guess = int(input("\nMake your guess:\n"))
        if user_guess == secret_number:
            print("That's correct! You've made the right guess!")
            continue_game = False
        elif user_guess < secret_number:
            attempts_remaining -= 1
            # print("Too Low")
            print(f"Too Low. You've {attempts_remaining} attempts remaining.")
        elif user_guess > secret_number:
            attempts_remaining -= 1
            # print("Too High")
            print(f"Too High. You've {attempts_remaining} attempts remaining.")


number_guessing_game()
