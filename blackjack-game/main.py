import random

def deal_card():
    # Function to deal a random card from the deck
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    return random.choice(cards)

def calculate_score(cards):
    # Function to calculate the total score of a hand
    score = sum(cards)
    if score > 21 and 11 in cards:
        score -= 10  # Convert one Ace from 11 to 1
    return score

def blackjack():
    # Main game function
    player_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]

    print("Welcome to Blackjack!")

    while True:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        print("\nYour cards:", player_cards, "| Your score:", player_score)
        print("Dealer's card:", [dealer_cards[0]])

        if player_score == 21:
            print("Blackjack! You win!")
            break
        elif player_score > 21:
            print("Busted! You lose.")
            break

        action = input("Type 'hit' to get another card, or 'stand' to stop: ").lower()

        if action == "hit":
            player_cards.append(deal_card())
        elif action == "stand":
            while dealer_score < 17:
                dealer_cards.append(deal_card())
                dealer_score = calculate_score(dealer_cards)

            print("\nYour final hand:", player_cards, "| Your final score:", player_score)
            print("Dealer's final hand:", dealer_cards, "| Dealer's final score:", dealer_score)

            if dealer_score > 21 or dealer_score < player_score:
                print("You win!")
            elif dealer_score > player_score:
                print("Dealer wins!")
            else:
                print("It's a draw!")
            break
        else:
            print("Invalid action. Please type 'hit' or 'stand'.")

if __name__ == "__main__":
    blackjack()
