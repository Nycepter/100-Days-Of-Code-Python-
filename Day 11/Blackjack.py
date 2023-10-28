import random
deck = {
    'ace-clubs': [1, 11],
    'two-clubs': 2,
    'three-clubs': 3,
    'four-clubs': 4,
    'five-clubs': 5,
    'six-clubs': 6,
    'seven-clubs': 7,
    'eight-clubs': 8,
    'nine-clubs': 9,
    'ten-clubs': 10,
    'jack-clubs': 10,
    'queen-clubs': 10,
    'king-clubs': 10,
    'ace-hearts': [1, 11],
    'two-hearts': 2,
    'three-hearts': 3,
    'four-hearts': 4,
    'five-hearts': 5,
    'six-hearts': 6,
    'seven-hearts': 7,
    'eight-hearts': 8,
    'nine-hearts': 9,
    'ten-hearts': 10,
    'jack-hearts': 10,
    'queen-hearts': 10,
    'king-hearts': 10,
    'ace-spades': [1, 11],
    'two-spades': 2,
    'three-spades': 3,
    'four-spades': 4,
    'five-spades': 5,
    'six-spades': 6,
    'seven-spades': 7,
    'eight-spades': 8,
    'nine-spades': 9,
    'ten-spades': 10,
    'jack-spades': 10,
    'queen-spades': 10,
    'king-spades': 10,
    'ace-diamonds': [1, 11],
    'two-diamonds': 2,
    'three-diamonds': 3,
    'four-diamonds': 4,
    'five-diamonds': 5,
    'six-diamonds': 6,
    'seven-diamonds': 7,
    'eight-diamonds': 8,
    'nine-diamonds': 9,
    'ten-diamonds': 10,
    'jack-diamonds': 10,
    'queen-diamonds': 10,
    'king-diamonds': 10,
}

player = "player"
dealer = "dealer"
player_money = 1000
dealer_money = 1000000
reset = False


def deal(recipient):
    if recipient == player:
        player_cards = []
        player_score = 0
        for i in range(0, 2):
            draw = (random.choice(list(deck.keys())))
            player_cards.append(draw)
            if isinstance(deck[draw], list):
                if player_score + deck[draw][1] <= 21:
                    player_score += deck[draw][1]
                else:
                    player_score += deck[draw][0]
            else:
                player_score += int(deck[draw])
            del deck[draw]
        result = [player_cards, player_score]
        return result
    elif recipient == dealer:
        dealer_cards = []
        dealer_score = 0
        for i in range(0, 1):
            draw = (random.choice(list(deck.keys())))
            dealer_cards.append(draw)
            if isinstance(deck[draw], list):
                if dealer_score + deck[draw][1] <= 21:
                    dealer_score += deck[draw][1]
                else:
                    dealer_score += deck[draw][0]
            else:
                dealer_score += int(deck[draw])
            del deck[draw]
        result = [dealer_cards, dealer_score]
        return result


def hit(recipient):
    if recipient == player:
        player_cards = []
        player_score = 0

        draw = (random.choice(list(deck.keys())))
        player_cards.append(draw)
        if isinstance(deck[draw], list):
            if player_score + deck[draw][1] <= 21:
                player_score += deck[draw][1]
            else:
                player_score += deck[draw][0]
        else:
            player_score += int(deck[draw])
        del deck[draw]
        result = [player_cards, player_score]
        return result
    elif recipient == dealer:
        dealer_cards = []
        dealer_score = 0

        draw = (random.choice(list(deck.keys())))
        dealer_cards.append(draw)
        if isinstance(deck[draw], list):
            if dealer_score + deck[draw][1] <= 21:
                dealer_score += deck[draw][1]
            else:
                dealer_score += deck[draw][0]
        else:
            dealer_score += int(deck[draw])
        del deck[draw]
        result = [dealer_cards, dealer_score]
        return result


print("Welcome to blackjack! \n")

while True:
    while reset == True:
        deck = {
            'ace-clubs': [1, 11],
            'two-clubs': 2,
            'three-clubs': 3,
            'four-clubs': 4,
            'five-clubs': 5,
            'six-clubs': 6,
            'seven-clubs': 7,
            'eight-clubs': 8,
            'nine-clubs': 9,
            'ten-clubs': 10,
            'jack-clubs': 10,
            'queen-clubs': 10,
            'king-clubs': 10,
            'ace-hearts': [1, 11],
            'two-hearts': 2,
            'three-hearts': 3,
            'four-hearts': 4,
            'five-hearts': 5,
            'six-hearts': 6,
            'seven-hearts': 7,
            'eight-hearts': 8,
            'nine-hearts': 9,
            'ten-hearts': 10,
            'jack-hearts': 10,
            'queen-hearts': 10,
            'king-hearts': 10,
            'ace-spades': [1, 11],
            'two-spades': 2,
            'three-spades': 3,
            'four-spades': 4,
            'five-spades': 5,
            'six-spades': 6,
            'seven-spades': 7,
            'eight-spades': 8,
            'nine-spades': 9,
            'ten-spades': 10,
            'jack-spades': 10,
            'queen-spades': 10,
            'king-spades': 10,
            'ace-diamonds': [1, 11],
            'two-diamonds': 2,
            'three-diamonds': 3,
            'four-diamonds': 4,
            'five-diamonds': 5,
            'six-diamonds': 6,
            'seven-diamonds': 7,
            'eight-diamonds': 8,
            'nine-diamonds': 9,
            'ten-diamonds': 10,
            'jack-diamonds': 10,
            'queen-diamonds': 10,
            'king-diamonds': 10,
        }
        reset = False
        continue
    if dealer_money < 1:
        print("The dealer is out of money, you took it all!")
        exit()
    elif player_money < 1:
        print("You have no money left to bet, go home!")
        exit()
    player_bet = input
    choice1 = input("Play new round of blackjack? 'yes' or 'no'\n > ")
    if choice1 == "yes":
        while True:
            print(f"Your avaliable balance is ${player_money}")
            player_bet = int(
                input("How much money would you like to bet? \n > "))
            if player_bet > player_money:
                print("Please enter an amount you actually have.")
                continue
            elif player_bet < 1:
                print("Please bet money.")
                continue
            else:
                break

        result_player = []
        result_dealer = []
        result2_player = []
        result3_player = []
        player_score = 0
        player_cards = []
        dealer_score = 0
        dealer_cards = []

        initial_deal_player = deal(player)
        player_cards += initial_deal_player[0]
        player_score += initial_deal_player[1]

        print(
            f'Your cards are {player_cards}, worth {player_score} points.')

        initial_deal_dealer = deal(dealer)
        dealer_cards += initial_deal_dealer[0]
        dealer_score += initial_deal_dealer[1]
        print(
            f'Dealer card shown is {dealer_cards}, worth {dealer_score} points.')
        if player_score > 21:
            print("BUST, you lose!")
            player_money -= player_bet
            dealer_money += player_bet
            reset = True
            continue
        elif player_score == 21:
            print("You have a Blackjack!")

        choice2 = input("Would you like to 'hit' or 'stay'? \n > ")

        if choice2 == "hit":
            hit1 = hit(player)
            player_cards += hit1[0]
            player_score += hit1[1]
            print(
                f'Your cards are {player_cards}, worth {player_score}   points.')
            print(
                f'Dealer card shown is {dealer_cards}, worth {dealer_score} points.')
            if player_score > 21:
                print("BUST, you lose!")
                player_money -= player_bet
                dealer_money += player_bet
                reset = True
                continue
            elif player_score == 21:
                print("You have a Blackjack!")

            choice3 = input("Would you like to 'hit' or 'stay'? \n > ")
            if choice3 == "hit":
                hit2 = hit(player)
                player_cards += hit2[0]
                player_score += hit2[1]
                print(
                    f'Your cards are {player_cards}, worth {player_score}   points.')
                print(
                    f'Dealer card shown is {dealer_cards}, worth {dealer_score} points.')
                if player_score > 21:
                    print("BUST, you lose!")
                    player_money -= player_bet
                    dealer_money += player_bet
                    reset = True
                    continue
                elif player_score == 21:
                    print("You have a Blackjack!")

                choice4 = input(
                    "Would you like to 'hit' or 'stay'? \n > ")
                if choice4 == "hit":
                    hit3 = hit(player)
                    player_cards += hit3[0]
                    player_score += hit3[1]
                    print(
                        f'Your cards are {player_cards}, worth {player_score}   points.')
                    print(
                        'Dealer card shown is {dealer_cards}, worth {dealer_score} points.')
                    if player_score > 21:
                        print("BUST, you lose!")
                        player_money -= player_bet
                        dealer_money += player_bet
                        reset = True
                        continue
                    elif player_score == 21:
                        print("You have a Blackjack!")

                    while dealer_score < 17:
                        dealer_cards += hit(dealer)[0]
                        dealer_score += hit(dealer)[1]
                        print(
                            f'Your cards are {player_cards}, worth {player_score}   points.')
                        print(
                            f'Dealer cards are {dealer_cards}, worth {dealer_score} points.')
                        if player_score == dealer_score:
                            print("It's a draw!")
                            reset = True
                            continue
                        elif player_score == 21:
                            print("You win!")
                            player_money += player_bet
                            dealer_money -= player_bet
                            reset = True
                            continue
                        elif dealer_score == 21:
                            print("You lose!")
                            player_money -= player_bet
                            dealer_money += player_bet
                            reset = True
                            continue
                        elif dealer_score > 21:
                            print("Dealer busts, you win!")
                            player_money += player_bet
                            dealer_money -= player_bet
                            reset = True
                            continue
                        elif 21 - player_score < 21 - dealer_score:
                            print("You win!")
                            player_money += player_bet
                            dealer_money -= player_bet
                            reset = True
                            continue
                        elif 21 - player_score > 21 - dealer_score:
                            print("You lose!")
                            player_money -= player_bet
                            dealer_money += player_bet
                            reset = True
                            continue

                elif choice4 == "stay":
                    while dealer_score < 17:
                        dealer_cards += hit(dealer)[0]
                        dealer_score += hit(dealer)[1]
                    print(
                        f'Your cards are {player_cards}, worth {player_score}   points.')
                    print(
                        f'Dealer cards are {dealer_cards}, worth {dealer_score} points.')
                    if player_score == dealer_score:
                        print("It's a draw!")
                        reset = True
                        continue
                    elif player_score == 21:
                        print("You win!")
                        player_money += player_bet
                        dealer_money -= player_bet
                        reset = True
                        continue
                    elif dealer_score == 21:
                        print("You lose!")
                        player_money -= player_bet
                        dealer_money += player_bet
                        reset = True
                        continue
                    elif dealer_score > 21:
                        print("Dealer busts, you win!")
                        player_money += player_bet
                        dealer_money -= player_bet
                        reset = True
                        continue
                    elif 21 - player_score < 21 - dealer_score:
                        print("You win!")
                        player_money += player_bet
                        dealer_money -= player_bet
                        reset = True
                        continue
                    elif 21 - player_score > 21 - dealer_score:
                        print("You lose!")
                        player_money -= player_bet
                        dealer_money += player_bet
                        reset = True
                        continue

            elif choice3 == "stay":
                while dealer_score < 17:
                    dealer_cards += hit(dealer)[0]
                    dealer_score += hit(dealer)[1]
                print(
                    f'Your cards are {player_cards}, worth {player_score}   points.')
                print(
                    f'Dealer cards are {dealer_cards}, worth {dealer_score} points.')
                if player_score == dealer_score:
                    print("It's a draw!")
                    reset = True
                    continue
                elif player_score == 21:
                    print("You win!")
                    player_money += player_bet
                    dealer_money -= player_bet
                    reset = True
                    continue
                elif dealer_score == 21:
                    print("You lose!")
                    player_money -= player_bet
                    dealer_money += player_bet
                    reset = True
                    continue
                elif dealer_score > 21:
                    print("Dealer busts, you win!")
                    player_money += player_bet
                    dealer_money -= player_bet
                    reset = True
                    continue
                elif 21 - player_score < 21 - dealer_score:
                    print("You win!")
                    player_money += player_bet
                    dealer_money -= player_bet
                    reset = True
                    continue
                elif 21 - player_score > 21 - dealer_score:
                    print("You lose!")
                    player_money -= player_bet
                    dealer_money += player_bet
                    reset = True
                    continue
        elif choice2 == "stay":
            while dealer_score < 17:
                dealer_cards += hit(dealer)[0]
                dealer_score += hit(dealer)[1]
            print(
                f'Your cards are {player_cards}, worth {player_score}   points.')
            print(
                f'Dealer cards are {dealer_cards}, worth {dealer_score} points.')
            if player_score == dealer_score:
                print("It's a draw!")
                reset = True
                continue
            elif player_score == 21:
                print("You win!")
                player_money += player_bet
                dealer_money -= player_bet
                reset = True
                continue
            elif dealer_score == 21:
                print("You lose!")
                player_money -= player_bet
                dealer_money += player_bet
                reset = True
                continue
            elif dealer_score > 21:
                print("Dealer busts, you win!")
                player_money += player_bet
                dealer_money -= player_bet
                reset = True
                continue
            elif 21 - player_score < 21 - dealer_score:
                print("You win!")
                player_money += player_bet
                dealer_money -= player_bet
                reset = True

                continue
            elif 21 - player_score > 21 - dealer_score:
                print("You lose!")
                player_money -= player_bet
                dealer_money += player_bet
                reset = True
                continue
    elif choice2 == "no":
        exit()
