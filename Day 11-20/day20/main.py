# Snake Game Part 1
from turtle import Screen
from snake import Snake
import time

snake = Snake()

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)
screen.listen()
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down,"Down")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right,"Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
