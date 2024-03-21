from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-290, 260)
        self.update_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def update_score(self):
        self.write(f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(-290, 220)
        self.color("red")
        self.write(f"GAME OVER!!", align=ALIGNMENT, font=FONT)
