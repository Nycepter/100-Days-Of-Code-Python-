import random
print("Welcome to the number guessing game! I think of a number from 1 to 100, and you try to guess it!")


def difficulty(input):
    if input == "easy":
        LIVES = 10
    elif input == "hard":
        LIVES = 5
    elif input == "ironman":
        LIVES = 1
    return LIVES


def Guessing_Game():
    Score = 0
    correct_guesses = 0
    incorrect_guesses = 0
    Scoreadd = 0
    while True:
        Win = False
        LIVES = difficulty(input(
            "\nDo you want to play on 'Easy', 'Hard', or 'Ironman'? \n").lower())
        if LIVES == 1:
            Scoreadd = 1000
        elif LIVES == 5:
            Scoreadd = 100
        else:
            Scoreadd = 10

        while LIVES > 0 and Win == False:
            Number = random.randrange(1, 101)
            print(f"Guesses remaining: {LIVES}")
            while LIVES > 0:
                Guess = int(input("Please enter your guess. \n\n"))
                if Guess > Number:
                    LIVES -= 1
                    print("Your guess is too high.")
                    print(f"Guesses remaining: {LIVES}")
                    continue
                elif Guess < Number:
                    LIVES -= 1
                    print("Your guess is too low.")
                    print(f"Guesses remaining: {LIVES}")
                    continue
                elif Guess == Number:
                    correct_guesses += 1
                    Score += Scoreadd
                    print("That is the number, you win!")
                    print(
                        f"Score: {Score / (correct_guesses + incorrect_guesses)}")
                    print(f"Wins: {correct_guesses}")
                    print(f"Losses: {incorrect_guesses}")
                    Win = True
                    break

        if LIVES > 0 and Win == True:
            continue

        else:
            incorrect_guesses += 1
            print("You are out of guesses, you lose!\n\n")
            print(
                f"Score: {Score / (correct_guesses + incorrect_guesses)}")
            print(f"Wins: {correct_guesses}")
            print(f"Losses: {incorrect_guesses}")
            continue


Guessing_Game()
