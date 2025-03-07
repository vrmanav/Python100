# Blackjack Game Rules:
# The goal of the game is to beat the dealer's hand without going over 21.
# Face cards (Kings, Queens, and Jacks) are worth 10 points. ✅
# Aces are worth 1 or 11 points, whichever makes a better hand. ✅
# Each player starts with two cards, one of the dealer's cards is hidden until the end. ✅
# Players can choose to "Hit" to take another card or "Stand" to hold their total and end their turn. ✅
# If a player goes over 21 points, they "bust" and lose the game.
# The dealer must hit until their cards total 17 or higher.
# If the dealer busts, all remaining players win.
# If neither the player nor the dealer busts, the higher hand wins.

import random


def deal_card():
    """Returns a card from deck"""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "\nIt's a DRAW"
    elif computer_score == 0:
        return "\nYou LOSE. Dealer has a BlackJack"
    elif user_score == 0:
        return "\nYou WIN. You have a BlackJack"
    elif user_score > 21:
        return "\nYou LOSE. You went over"
    elif computer_score > 21:
        return "\nYou WIN. Dealer went over"
    elif user_score > computer_score:
        return "\n You WIN."
    else:
        return "\nYou LOSE."


def blackjack():
    print("♠️ Welcome to Blackjack Game ♣️")
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    continue_game = True

    for card in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while continue_game:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\nYour cards {user_cards} with score {user_score}")
        print(f"Computer's first card {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            continue_game = False
        else:
            user_hit = input("Do you want to take another card, type HIT, else type STAND: ").lower()
            if user_hit == "hit":
                user_cards.append(deal_card())
            else:
                do_continue = False

    while computer_score != 0 or computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand {user_cards} with score {user_score}")
    print(f"Dealer final hand {computer_cards} with score {computer_score}")
    print(compare(user_score, computer_score))


blackjack()
