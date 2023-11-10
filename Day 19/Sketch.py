from turtle import Turtle, Screen

turt = Turtle()
screen = Screen()


def move_forward():
    turt.forward(10)


def move_backward():
    turt.backward(10)


def rotateright():
    turt.right(10)


def rotateleft():
    turt.left(10)


def reset():
    turt.reset()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=rotateleft)
screen.onkey(key="d", fun=rotateright)
screen.onkey(key="c", fun=reset)
screen.exitonclick()
