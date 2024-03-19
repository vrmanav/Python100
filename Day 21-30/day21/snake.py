from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
STEP = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        for position in STARTING_POS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[segment_number - 1].xcor()
            y_cor = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(x_cor, y_cor)
        self.head.forward(STEP)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        self.add_segment(self.segments[-1].position())
