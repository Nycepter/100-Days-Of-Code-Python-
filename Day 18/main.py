from turtle import Turtle, Screen
import random

colors = ["red", "green", "blue", "orange", "purple", "pink",
          "yellow", "black", "magenta", "crimson", "maroon"]

jake = Turtle()
jake.shape("turtle")
jake.color("chartreuse4")
line_number = 3
dist = 100


while line_number < 100:
    jake.color(random.choice(colors))
    deg = 360 / line_number

    for i in range(line_number):
        if line_number % 4 == 0:
            jake.forward(100)
            jake.right(deg)
        elif line_number % 3 == 0:
            jake.backward(100)
            jake.right(deg)
        elif line_number % 2 == 0:
            jake.forward(100)
            jake.left(deg)
        else:
            jake.backward(100)
            jake.left(deg)

    line_number += 1
    continue


screen = Screen()
screen.setup(width=2000, height=1200)
screen.exitonclick()
