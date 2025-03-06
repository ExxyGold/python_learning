from pi_art import auction_logo
import os
def clear():
    os.system('cls')

print(auction_logo)

print("Welcome to Secret Auction Program")

done_bidding = False
details = {}
def evaluate(assembled):
    winner= ""
    highest = 0
    for bidder in assembled:
        if assembled[bidder] > highest:
            highest = assembled[bidder]
            winner = bidder
    print(f"The bid winner is {winner} with bid price ${highest}")

while not done_bidding:
    name = input("What is your name:")
    bid = int(input("What is your bid price: $"))

    details [name] = bid

    finish = input("Are there any other bidders? Type 'Yes' or 'No': ").lower()
    
    if finish == "no":
        done_bidding = True
        clear()
        evaluate(details)
    else:
        clear()



