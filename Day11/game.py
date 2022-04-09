import random
from art import logo

game_on = input('Do you want to play a game of Blackjack? Type "y" for Yes and "n" for No?')

def pick_a_card(cards):
    card = random.choice(cards)
    return card

def show(player_cards, dealer_cards, begin=False):
    player_score = sum(player_cards)
    dealer_score = sum(dealer_cards)
    
    if begin:
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_score}")

    else:
        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
        if player_score > 21:
            print("You went bust! You lose. 🥲")
        elif player_score < 21:
            if dealer_score == 21:
                print("Dealer has a blackjack. You lose!🥺")
            elif player_score > dealer_score:
                print("You win!🎉")
            else:
                print("You lose!😤")
        else:
            print("You have a blackjack. You win!💵")

    
if game_on == 'y':
    print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealer_cards = []
    player_cards = []

    player_cards.append(pick_a_card(cards))
    player_cards.append(pick_a_card(cards))
    dealer_cards.append(pick_a_card(cards))

    show(player_cards, dealer_cards, True)

    pick_another = input("Type 'y' to get another card, type 'n' to pass:")
    while pick_another == 'y':
        pick_another = input("Type 'y' to get another card, type 'n' to pass:")
        player_cards.append(pick_a_card(cards))
        
    else:
        while sum(dealer_cards) < 17:
            dealer_cards.append(pick_a_card(cards))
    
    show(player_cards, dealer_cards)

else:
    print("It was a pleasure to have you here!")
