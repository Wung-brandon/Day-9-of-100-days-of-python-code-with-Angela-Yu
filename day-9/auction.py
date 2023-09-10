
from replit import clear

def find_highest_bidder(bidding_record):
    highest_amount = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_amount:
            highest_amount = bid_amount
            winner = bidder
    print(f'The winner is {winner} with an amount of {highest_amount}$')
    

       
any_bidders = True
while any_bidders:
    name = input("Enter your name: ")
    bid_price = int(input("Enter your bid price $:"))
    
    auction = {}
    auction[name] = bid_price
    print(auction)
    bidders = input("Are they any bidders? Type 'yes' or 'no':").lower()
    if bidders == 'yes':
        #clear()
        pass
    elif bidders == 'no':
        any_bidders = False
        find_highest_bidder(auction) 
        
        
    #print(auction)


