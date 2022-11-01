from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.


bids = {}

def get_highest_bid(highest_bidder):
    highest_bid = 0
    for bid in highest_bidder:
        bid_amount = highest_bidder[bid]
        if bid_amount  > highest_bid:
            highest_bid = bid_amount
            winner = bid

    print(f"The winner is {winner} and they won with ${bid_amount}")
are_there_more_bidders = True
while are_there_more_bidders:
    print(logo)
    name = input("Type your name\n")
    bid_price =  float(input("Enter your bid. $"))

    bids[name] = bid_price
    more_bidders = input("Are there any more bidders in the room. Type yes or no.\n")
    if more_bidders == "no":
        are_there_more_bidders = False
        # highest_bidder = max(bids,key=bids.get)
        get_highest_bid(bids)
    else:
        clear()


