# Blackjack Game Rules:
# The goal of the game is to beat the dealer's hand without going over 21.
# Face cards (Kings, Queens, and Jacks) are worth 10 points. ✅
# Aces are worth 1 or 11 points, whichever makes a better hand.
# Each player starts with two cards, one of the dealer's cards is hidden until the end. ✅
# Players can choose to "Hit" to take another card or "Stand" to hold their total and end their turn.
# If a player goes over 21 points, they "bust" and lose the game.
# The dealer must hit until their cards total 17 or higher.
# If the dealer busts, all remaining players win.
# If neither the player nor the dealer busts, the higher hand wins.

import random


def deal_card():
    """Returns a card from deck"""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def blackjack():
    print("♠️ Welcome to Blackjack Game ♣️")
    user_cards = []
    computer_cards = []
    for card in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    print(f"\nYour cards {user_cards} with score {user_score}")

blackjack()