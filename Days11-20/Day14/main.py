import random
from data import game_data
from os import system
from time import sleep


def format_data(person):
    name = person["name"]
    desc = person["description"].lower()
    country = person["country"]
    return f"{name}, a {desc}, from {country}"


def check_answer(user_guess, pA_follower_count, pB_follower_count):
    if pA_follower_count > pB_follower_count:
        return user_guess == "a"
    else:
        return user_guess == "b"


# 'pA' stands for person A
# 'pB' stands for person B
score = 0
pB = random.choice(game_data)
continue_game = True
while continue_game:
    system("clear")
    pA = pB
    if pA == pB:
        pB = random.choice(game_data)
    pA_follower_count = pA["follower_count"]
    pB_follower_count = pB["follower_count"]

    print(f"Compare\n\t A: {format_data(pA)} {pA["follower_count"]}")
    print(f"Against\n\t B: {format_data(pB)} {pB["follower_count"]}")
    user_guess = input("\nWho has more followers [A/B]:\n").lower()
    is_correct = check_answer(user_guess, pA_follower_count, pB_follower_count)
    if is_correct:
        score += 1
        print(f"\nCORRECT 🎉 Your current score is {score}")
        sleep(2)
    else:
        print(f"\nINCORRECT ‼️  Your final score is {score}")
        continue_game = False
