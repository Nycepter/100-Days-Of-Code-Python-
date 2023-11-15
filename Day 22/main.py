from turtle import Screen
from turtle import Turtle
from paddle import Paddle


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Nycepter's Pong")
screen.tracer(0)


paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))

screen.listen()
screen.onkey(paddle1.move_up, "Up")
screen.onkey(paddle1.move_down, "Down")

screen.listen()
screen.onkey(paddle2.move_up, "w")
screen.onkey(paddle2.move_down, "s")


game_is_on = True
while game_is_on == True:
    screen.update()

screen.exitonclick()
