from turtle import Turtle, Screen
import turtle
import time

X_POSITIONS = [20, 0, -20]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for snake_index in range(3):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(X_POSITIONS[snake_index], 0)
            self.segments.append(snake)

    def move(self):
        for snake_seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[snake_seg - 1].xcor()
            new_y = self.segments[snake_seg - 1].ycor()
            self.segments[snake_seg].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
