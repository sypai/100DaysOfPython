from art import logo
import os

clear = lambda: os.system('clear')

# Starting the auction with logo
print("Welcome to Bajpai Island!\nWe are here to auction paintings by Suyash Bajpai!")
print(logo)
print("\n==============================================================")

# Items Dictionary
paintings = {"Mona Lisa" : None, "Invincible": None, "La Lisa": None, "Legendary": None}
paintings_sold_info = paintings.copy()

painting_list = list(paintings.keys())
numOfItems = len(painting_list)

def ask():
    bidder = input("What is your name?")
    bid = int(input(("What is your bid: $")))
    bidder_available = input("Is there any other bidder for this painting?\nType 'yes/y' or 'no/n")
    return bidder, bid, bidder_available

# Check a list of dictionaries for the maximum bid 
def decide(info):
    maxBid = 0 
    maxBidIdx = -1
    for idx, bidder in enumerate(info):
        currBid = int(bidder['bid'])
        if currBid > maxBid:
            maxBid = currBid
            maxBidIdx = idx
    return info[maxBidIdx]

while numOfItems > 0:
    currItemNum = 5 - numOfItems
    print(f"Bid for Painting#{currItemNum}")
    print(f"This painting is called: {painting_list[currItemNum-1]}")
    bidder_available = input("Is there any bidder for this painting?\nType 'yes/y' or 'no/n'\n")
    if bidder_available == 'yes' or bidder_available == 'y':
        info = []
        while True:
            if bidder_available == 'yes' or bidder_available == 'y':     
                name, amount, bidder_available = ask()
                print("")
                info.append({'name': name, 'bid': amount})
            else:
                break
            paintings[painting_list[currItemNum-1]] = info
            clear()
    else:
        print("=======================================================")
        numOfItems -= 1
        continue
    print("=======================================================")
    paintings_sold_info[painting_list[currItemNum-1]] = decide(paintings[painting_list[currItemNum-1]])
    numOfItems -= 1
    clear()
    
# Pretty Print
numOfItems = len(painting_list)
print("Auction Ends! Immense Gratitude for Mr. Suyash Bajpai.\nThank you all for coming.\nCongratulations to all the buyers.")
while numOfItems > 0:
    currItemNum = 5 - numOfItems
    print(f"\n#{currItemNum}")
    if paintings_sold_info[painting_list[currItemNum-1]] is None:
        print(f"{painting_list[currItemNum-1]} remains unsold!")
        numOfItems -= 1
        continue
    print(f"{painting_list[currItemNum-1]} sold to {paintings_sold_info[painting_list[currItemNum-1]]['name']} for ${paintings_sold_info[painting_list[currItemNum-1]]['bid']}")
    numOfItems -= 1