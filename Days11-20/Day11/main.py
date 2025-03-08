import random


def give_cards():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def show_result(user_score, dealer_score):
    if user_score == dealer_score:
        return "It's a Draw"
    elif dealer_score == 0:
        return "You lose, dealer has Blackjack"
    elif user_score == 0:
        return "You win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif dealer_score > 21:
        return "Dealer went over. You win"
    elif user_score > dealer_score:
        return "You win"
    else:
        return "You lose"


def blackjack():
    user_cards = []
    dealer_cards = []
    game_not_over = True

    # Give initial 2 cards to dealer & user
    for card in range(2):
        user_cards.append(give_cards())
        dealer_cards.append(give_cards())

    while game_not_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        if user_score > 21:
            game_not_over = False
        else:
            print(f"\nYour cards are {user_cards} with score {user_score}")
            print(f"Dealer's first card is [{dealer_cards[0]}]")
            user_hit = input("To get another card type 'HIT', else 'STAND': ").lower()
            if user_hit == "hit":
                user_cards.append(give_cards())
            else:
                game_not_over = False

    while dealer_score < 17:
        dealer_cards.append(give_cards())
        dealer_score = calculate_score(dealer_cards)
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(show_result(user_score, dealer_score))


blackjack()
