import art

# Dictionary
bids = {}
# Boolean for continuing
continue_bids = True


# Function to clear console
def clear():
    print("\033c", end="", flush=True)

# Add a bidder to dictionary
def add_bidder():
    print(art.logo)
    name = input("What is your name?: ")

    while True:
        try:
            bid = int(input("What's your bid?: $"))
        except ValueError:
            print("Please enter a whole number!")
            continue
        else:
            break

    bids[name] = bid

# Prompt to add another bidder
def add_another():
    prompt = input("Are there any other users who would like to bid? (y/n) ").lower()
    if prompt == "y":
        return True
    elif prompt == "n":
        return False
    else:
        print("Please enter 'y' or 'n'.")
        add_another()

# Find highest bid
def find_highest(bids):
    highest_bid = 0
    highest_bidder = ""
    for user in bids:
        print(user)
        print(bids[user])
        if bids[user] > highest_bid:
            highest_bid = bids[user]
            highest_bidder = user
    clear()
    print(art.logo)
    print(f"{highest_bidder} is the highest bidder with a bid of ${highest_bid}!")    
    

# While bids are being taken
while continue_bids == True:
    # Clear console
    clear()
    # Functions
    add_bidder()
    continue_bids = add_another()
    print(continue_bids)

# End of bids
find_highest(bids)

