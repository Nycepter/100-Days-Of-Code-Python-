from turtle import Turtle

score = 0


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0, 265)
        self.write(f"Score: {self.score}", align="center",
                   font=("Arial", 24, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center",
                   font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center",
                   font=("Arial", 24, "normal"))
