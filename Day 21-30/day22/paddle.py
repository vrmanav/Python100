from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.penup()
        self.goto(position)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)

    def go_up(self):
        new_y_cor = self.ycor() + 20
        self.goto(self.xcor(), new_y_cor)

    def go_down(self):
        new_y_cor = self.ycor() - 20
        self.goto(self.xcor(), new_y_cor)
