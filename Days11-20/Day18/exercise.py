from turtle import Turtle, Screen
import random

tim = Turtle("turtle")
colors = [
    "cyan",
    "deep sky blue",
    "orange red",
    "yellow",
    "dark violet",
    "deep pink",
    "lavender",
    "spring green",
]

# * Exercise 1
# for step in range(4):
#     tim.forward(100)
#     tim.left(90)

# * Exercise 2
# import heroes
# import villains

# print(f"'{heroes.gen()}' V/S '{villains.gen()}'")

# * Exercise 3
# for step in range(20):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()


# * Exercise 4 - Shape maker
# def draw_shape(no_of_sides):
#     for step in range(no_of_sides):
#         tim.forward(100)
#         tim.right(360 / no_of_sides)
# for sides in range(3, 8):
#     tim.color(random.choice(colors))
#     draw_shape(sides)


# * Exercise 5 - Random walk generator
# directions = [0, 90, 180, 270]
# tim.hideturtle()
# tim.speed(10)
# tim.pensize(15)
# for step in range(200):
#     tim.color(random.choice(colors))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
