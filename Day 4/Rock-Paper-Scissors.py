import random
Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
Computer_Choices = ["Rock", "Paper", "Scissors"]
print("Let's play Rock, Paper, Scissors!\n")
User_Score = 0
Computer_Score = 0
Draws = 0


while True:
    print(f"Player Wins: {User_Score}")
    print(f"Computer Wins: {Computer_Score}")
    print(f"Draws: {Draws}")

    Prompt = input(
        "Would you like to choose 'Rock' 'Paper' or 'Scissors'?\n")
    User_Choice = Prompt.lower()
    Computer_Choice_R = random.choice(Computer_Choices)
    Computer_Choice = Computer_Choice_R.lower()
    if User_Choice == "rock":
        print(f"\nYou chose {User_Choice}. \n {Rock}\n")
    elif User_Choice == "paper":
        print(f"\nYou chose {User_Choice}. \n {Paper}\n")
    else:
        print(f"\nYou chose {User_Choice}. \n {Scissors}\n")

    if Computer_Choice == "rock":
        print(f"Computer chose {Computer_Choice}. \n {Rock}\n")
    elif Computer_Choice == "paper":
        print(f"Computer chose {Computer_Choice}. \n {Paper}\n")
    else:
        print(f"Computer chose {Computer_Choice}. \n {Scissors}\n")

    if User_Choice == "rock" and Computer_Choice == "paper":
        print("The computer wins!\n")
        Computer_Score += 1
        continue
    elif User_Choice == "rock" and Computer_Choice == "rock":
        print("It's a Draw, try again!\n")
        Draws += 1
        continue
    elif User_Choice == "rock" and Computer_Choice == "scissors":
        print('You win!\n')
        User_Score += 1
        continue
    elif User_Choice == "paper" and Computer_Choice == "paper":
        print("It's a Draw, try again!\n")
        Draws += 1
        continue
    elif User_Choice == "paper" and Computer_Choice == "rock":
        print("You win!\n")
        User_Score += 1
        continue
    elif User_Choice == "paper" and Computer_Choice == "scissors":
        print("The computer wins!\n")
        Computer_Score += 1
        continue
    elif User_Choice == "scissors" and Computer_Choice == "scissors":
        print("It's a Draw, try again!\n")
        Draws += 1
        continue
    elif User_Choice == "scissors" and Computer_Choice == "paper":
        print("You win!\n")
        User_Score += 1
        continue
    elif User_Choice == "scissors" and Computer_Choice == "rock":
        print("The computer wins!\n")
        Computer_Score += 1
        continue
