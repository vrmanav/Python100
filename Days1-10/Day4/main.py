from art import rock, paper, scissors
import random
from os import system

symbols = [rock, paper, scissors]

print("Welcome to Rock-Paper-Scissors")
print("------- -- -------------------")
print("\n0: Rock\n1: Paper\n2: Scissors")

user_choice = int(input("\nWhat do you choose?\n"))
computer_choice = random.randint(0, 2)
if user_choice>=0 and user_choice<=2:
    system("clear")
    print(symbols[user_choice])
print("\nComputer chose")
print(symbols[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You have typed invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You Lose!")
elif computer_choice == 0 and user_choice == 2:
    print("🎉 You Win 🎉")
elif computer_choice > user_choice:
    print("You Lose!")
elif user_choice > computer_choice:
    print("🎉You Win 🎉")
elif computer_choice == user_choice:
    print("It's a tie!")
