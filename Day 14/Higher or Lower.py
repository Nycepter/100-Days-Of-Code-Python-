from HOLdata import data
from HOLart import logo
from HOLart import vs
import random


def Get_Opponent1():
    Opponent1 = random.choice(data)
    Name = Opponent1['name']
    Follower_Count = int(Opponent1['follower_count'])
    Profession = Opponent1['description']
    Origin = Opponent1['country']
    print(f"Compare A: {Name}, a {Profession}, from {Origin}.")
    return Follower_Count


def Get_Opponent2():
    Opponent2 = random.choice(data)
    Name = Opponent2['name']
    Follower_Count = int(Opponent2['follower_count'])
    Profession = Opponent2['description']
    Origin = Opponent2['country']
    print(f"Against B: {Name}, a {Profession}, from {Origin}.")
    return Follower_Count


def Compare():
    Score = 0
    High_Score = 0
    print("Welcome to")
    print(logo)
    while True:
        print(f"Your current score is: {Score}.")
        print(f"Your current high-score is: {High_Score}\n")
        Opponent1 = Get_Opponent1()
        print(vs)
        Opponent2 = Get_Opponent2()
        Guess = input("Who has more followers? 'A', or 'B'? \n> ").lower()
        if Guess == "a" and Opponent1 > Opponent2:
            if High_Score <= Score:
                High_Score = Score + 1
            Score += 1
            print("\nThat is correct!")
            continue
        elif Guess == "b" and Opponent1 < Opponent2:
            if High_Score <= Score:
                High_Score = Score + 1
            Score += 1
            print("\nThat is correct!")
            continue
        else:
            print(f"\nThat is incorrect, you lose! Your score was {Score}\n")
            Score = 0
            continue


Compare()
