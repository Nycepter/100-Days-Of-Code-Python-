import random
print("Welcome to the number guessing game! I think of a number from 1 to 100, and you try to guess it!")
Score = 0
correct_guesses = 0
incorrect_guesses = 0
while True:
    LIVES = 10
    Win = False
    difficulty = input(
        "\nDo you want to play on 'Easy', 'Hard', or 'Ironman'? \n").lower()
    while LIVES > 0 and Win == False:
        if difficulty == "easy":
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
                    Score += 10
                    print("That is the number, you win!")
                    print(
                        f"Score: {Score / (correct_guesses + incorrect_guesses)}")
                    print(f"Wins: {correct_guesses}")
                    print(f"Losses: {incorrect_guesses}")
                    Win = True
                    break
            else:
                continue
        if difficulty == "hard":
            LIVES = 5
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
                    Score += 10
                    print("That is the number, you win!")
                    print(
                        f"Score: {Score / (correct_guesses + incorrect_guesses)}")
                    print(f"Wins: {correct_guesses}")
                    print(f"Losses: {incorrect_guesses}")
                    Win = True
                    break
            else:
                continue
        if difficulty == "ironman":
            LIVES = 1
            Number = random.randrange(1, 101)
            print(f"Guesses remaining: {LIVES}")
            while LIVES > 0:
                Guess = int(input("Please enter your guess. \n\n"))
                if Guess > Number:
                    LIVES -= 1
                    print("Your guess is too high.")
                    continue
                elif Guess < Number:
                    LIVES -= 1
                    print("Your guess is too low.")
                    continue
                elif Guess == Number:
                    correct_guesses += 1
                    Score += 10
                    print("That is the number, you win!")
                    print(
                        f"Score: {Score / (correct_guesses + incorrect_guesses)}")
                    print(f"Wins: {correct_guesses}")
                    print(f"Losses: {incorrect_guesses}")
                    Win = True
                    break
            else:
                continue
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
