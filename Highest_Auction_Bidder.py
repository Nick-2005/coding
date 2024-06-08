
def highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
finished = False
while not finished:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
    bids[name] = bid
    more_bidders = input("Are there any more bidders? Type 'yes' or 'no': ")
    if more_bidders == "yes":
        continue
    if more_bidders == "no":
        finished = True
        highest_bidder(bids)
