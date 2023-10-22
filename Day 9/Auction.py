import os
# os.system('clear')
auction_participants = {
}


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def auction_list(name, bid):
    auction_participants[name] = bid


print("Welcome to the auction!")
while True:
    answer = input("Would you like to place a bid?\n").lower()
    if answer == "yes":
        clear_console()
        name = input("Enter your name. \n")
        clear_console()
        bid = int(input("Enter your bid. \n"))
        clear_console()
        auction_list(name, bid)
        clear_console()
    if answer == "no":
        clear_console()
        highest_bid = max(auction_participants.values())
        highest_bidder = max(auction_participants,
                             key=auction_participants.get)
        print(
            f"This concludes the auction! \n{highest_bidder} won the auction with a bid of ${highest_bid}.")

        break
