############### Blackjack Project #####################

# Blackjack game: https://games.washingtonpost.com/games/blackjack/

# Project requirements: http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF

# Project flow chart: https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt


############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.


import random


# Function to deal a random card from the deck
def deal_card():
    """Returns a random card from the list."""
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(deck)
    return card


# Function to calculate the score of a given hand of cards
def calculate_score(hand):
    """Calculates User and Computer Scores."""

    # Check for a blackjack (a hand with 21 and exactly two cards)
    if sum(hand) == 21 and len(hand) == 2:
        return 0

    # Adjust for ace value if score is over 21
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return sum(hand)


# Function to compare the final scores of the player and the dealer
def compare_scores(player_score, dealer_score):
    if player_score == dealer_score:
        return "Draw"
    elif dealer_score == 0:
        return "Lose, opponent has blackjack"
    elif player_score == 0:
        return "Win with a blackjack"
    elif player_score > 21:
        return "You went over, you lose"
    elif dealer_score > 21:
        return "Opponent went over, you win"
    elif player_score > dealer_score:
        return "You win"
    else:
        return "You lose"


# Initialize hands for player and dealer
player_hand = []
dealer_hand = []
game_over = False

# Deal initial two cards to both player and dealer
for _ in range(2):
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())

# Player's turn: Continue to prompt player for more cards until they decide to stop or go bust
while not game_over:
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    print(f" Your cards: {player_hand}, Your score: {player_score}")
    print(f" Dealer's card: {dealer_hand[0]}, Dealer's score: {dealer_score}")

    if player_score == 0 or dealer_score == 0 or player_score > 21:
        game_over = True
    else:
        player_choice = input("Type 'y' to get another card or 'n' to pass: ")
        if player_choice == 'y':
            player_hand.append(deal_card())
        else:
            game_over = True

# Dealer's turn: Continue to draw cards until the score reaches at least 17
while dealer_score != 0 and dealer_score < 17:
    dealer_hand.append(deal_card())
    dealer_score = calculate_score(dealer_hand)

# Compare final scores and determine the result
print(compare_scores(player_score, dealer_score))

