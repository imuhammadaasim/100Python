from art import logo
import os

def clear_console():
    # ANSI escape sequence to clear screen
    print('\033[H\033[J')

print(logo)

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    max_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > max_bid:
            max_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${max_bid}")


while not bidding_finished:
    name = input("Enter name of the bidder: ")
    bid = int(input("Enter the amount of bid: "))
    bids[name] = bid
    should_continue = input("Is there any other bidder? Type 'yes' or 'no'\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        clear_console()
