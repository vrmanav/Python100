from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.start()

    def start(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        self.forward(10)

    def go_down(self):
        self.backward(10)
