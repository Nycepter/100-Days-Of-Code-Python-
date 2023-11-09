from turtle import Turtle, Screen
import turtle
import random

colors = ["red", "green", "blue", "orange", "purple", "pink",
          "yellow", "black", "magenta", "crimson", "maroon"]

jake = Turtle()
jake.shape("turtle")
jake.color("chartreuse4")
angles = [0, 90, 180, 270]
jake.pensize(1)
jake.speed(0)

turtle.colormode(255)


# def randmov():
#     jake.right(random.choice(angles))


def randomcolor():
    return random.randint(0, 255)


for i in range(360):
    jake.color(randomcolor(), randomcolor(), randomcolor())
    jake.circle(200)
    jake.right(1)


screen = Screen()
screen.setup(width=2000, height=1200)
screen.exitonclick()
