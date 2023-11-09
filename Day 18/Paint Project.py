import colorgram
from turtle import Turtle, Screen
import turtle
import random


color_list = []
colors = colorgram.extract('100-Days-Of-Code-Python-\Day 18\image.jpg', 10)

for color in colors:
    r, g, b = color.rgb.r, color.rgb.g, color.rgb.b
    if r < 240 and g < 240 and b < 240:
        color_list.append((r, g, b))


jake = Turtle()
jake.shape("turtle")
jake.color("chartreuse4")
angles = [0, 90, 180, 270]
jake.pensize(1)
jake.speed(0)

turtle.colormode(255)


def randomcolor():
    return random.choice(color_list)


def turnaround():
    jake.left(90)
    jake.forward(50)
    jake.left(90)
    jake.forward(50)


def turnaround2():
    jake.right(90)
    jake.forward(50)
    jake.right(90)
    jake.forward(50)


def run():
    dots = 0
    jake.penup()
    while dots < 101:
        for i in range(10):
            jake.dot(20, randomcolor())
            jake.forward(50)
        turnaround()
        for i in range(10):
            jake.dot(20, randomcolor())
            jake.forward(50)
        turnaround2()


run()


screen = Screen()
screen.setup(width=2000, height=1200)
screen.exitonclick()
