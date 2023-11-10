from turtle import Turtle, Screen
import random

is_race_going = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(
    "Make your bet.", "Which turtle will win? Enter a color.")
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range(6):
    turt = Turtle(shape="turtle")
    turt.color(colors[turtle_index])
    turt.penup()
    turt.goto(-230, y_positions[turtle_index])
    all_turtles.append(turt)

if user_bet:
    is_race_going = True

while is_race_going:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            print(f"{turtle.color()[0]} Wins!")
            if user_bet == turtle.color()[0]:
                print("You won the bet!")
            else:
                print("You lost the bet!")
            is_race_going = False
        distance = random.randint(0, 10)
        turtle.forward(distance)


screen.exitonclick()
