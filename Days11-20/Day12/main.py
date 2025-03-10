# Number guessing game
from random import randint

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def set_difficulty():
    difficulty = input("Choose difficulty [EASY/HARD]:\n")
    if difficulty == "easy":
        return EASY_ATTEMPTS
    elif difficulty == "hard":
        return HARD_ATTEMPTS


def check_answer(secret_number, user_guess, attempts):
    if user_guess == secret_number:
        print("\nThat's correct 🎉 You've made the right guess!")
    elif user_guess < secret_number:
        print(f"Too Low.")
        return attempts - 1
    elif user_guess > secret_number:
        print(f"Too High.")
        return attempts - 1


def number_guessing_game():
    print("* Welcome To Number Guessing Game *\n")
    print("I've thought of number between 1 and 100.")
    print("It's your task to make a correct guess of that number.\n")
    secret_number = randint(1, 101)
    print(secret_number)

    attempts = set_difficulty()
    user_guess = 0

    while user_guess != secret_number:
        print(f"You've {attempts} attempts to guess the number")
        user_guess = int(input("\nMake your guess:\n"))
        attempts = check_answer(secret_number, user_guess, attempts)
        if attempts == 0:
            print("\n⚠️ You run out of attempts. You lose! ⚠️")
            return


number_guessing_game()
