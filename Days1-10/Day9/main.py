from os import system


def find_highest_bidder(bidders):
    highest_bid = 0
    highest_bidder = ""
    for bidder in bidders:
        if bidders[bidder] > highest_bid:
            highest_bidder = bidder
            highest_bid = bidders[bidder]
    return highest_bidder


print("WELCOME TO SECRET AUCTION PROGRAM")
bidders = {}
stop_game = False

while not stop_game:
    bidder_name = input("\nWhat is your name?\n")
    bidder_bid = int(input("What is your bid? \n$"))
    bidders[bidder_name] = bidder_bid
    more_players = input("Are there any more bidders? [YES/NO]\n").lower()
    if more_players == "no":
        stop_game = True
    system("clear")

highest_bidder = find_highest_bidder(bidders)
print(f"Highest bidder is {highest_bidder}")
