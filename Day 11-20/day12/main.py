# Day 12: Number guessing game

from random import randint

HARD_ATTEMPTS = 5
EASY_ATTEMPTS = 10


def set_difficulty():
    difficulty = input("\nSelect level of difficulty. [EASY/HARD]:\n").lower()
    if difficulty == "easy":
        return EASY_ATTEMPTS
    elif difficulty == "hard":
        return HARD_ATTEMPTS


def check_answer(user_guess, secret_num, attempts):
    if user_guess > secret_num:
        print("\nToo High")
        return attempts - 1
    elif user_guess < secret_num:
        print("\nToo Low")
        return attempts - 1
    else:
        print("\n\t\t\tCONGRATULATIONS !! You've guessed the number")


def game():
    print("\t\t\tWELCOME TO NUMBER GUESSING GAME")
    print(
        "\n  I've guessed a number between 1 to 100. Your task is to find out the guessed number."
    )
    secret_num = randint(1, 100)
    attempts = set_difficulty()
    user_guess = 0
    while user_guess != secret_num:
        print(f"\nYou have {attempts} attempts left")
        user_guess = int(input("Make your guess:\n"))
        attempts = check_answer(user_guess, secret_num, attempts)
        if attempts == 0:
            print("\n\t\t\tYou've exhausted all your attempts. Better luck next time")
            break
        elif user_guess != secret_num:
            print("Guess again")


game()
