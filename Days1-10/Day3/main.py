print("Welcome to Treasure Island")

choice1 = input(
    "You are at a crossroad, where do you want to go? [LEFT / RIGHT]\n"
).lower()
if choice1 == "right":
    choice2 = input("You come to a lake. There is an island in the middle of the lake. [SWIM / WAIT]\n").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There are 3 doors. [RED / BLUE / GREEN]\n").lower()
        if choice3 == "red":
            print("You have reached the treasure. Don't forget my cut 😁")
        elif choice3 == "blue":
            print("It's a room full of fire 🔥 GAME OVER")
        elif choice3 == "green":
            print("There's a starving lion waiting just for you 😋 GAME OVER 🪦")
        else:
            print("Invalid input. Message from Yamraj: 'On my way' 🐂 GAME OVER 🪦")
    else:
        print("You got attacked by a hungry shark 🦈 GAME OVER 🪦")
else:
    print("You fell straight into hell 👹 GAME OVER 🪦")
