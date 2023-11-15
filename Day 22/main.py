from turtle import Screen
from turtle import Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Nycepter's Pong")
screen.tracer(0)


paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
pongball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle1.move_up, "Up")
screen.onkeypress(paddle1.move_down, "Down")

screen.listen()
screen.onkeypress(paddle2.move_up, "w")
screen.onkeypress(paddle2.move_down, "s")
speed = 0.1

game_is_on = True
while game_is_on == True:
    time.sleep(speed)
    screen.update()
    pongball.move()
    if pongball.ycor() >= 300 or pongball.ycor() <= -300:
        pongball.bounce()
    if ((pongball.distance(paddle1) < 50 and pongball.x_move > 0) or
            (pongball.distance(paddle2) < 50 and pongball.x_move < 0)):
        pongball.bounce2()
        speed *= .9
    if pongball.xcor() > 390 or pongball.xcor() < -390:
        if pongball.xcor() > 390:
            scoreboard.l_score += 1
        elif pongball.xcor() < -390:
            scoreboard.r_score += 1
        scoreboard.update_score()
        pongball.reset()
        speed = 0.1


screen.exitonclick()
