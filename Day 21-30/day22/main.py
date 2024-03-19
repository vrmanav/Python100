# Day 22: Ping Pong game

from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard
from turtle import Screen
from time import sleep

R_PADDLE_LOCATION = (350, 0)
L_PADDLE_LOCATION = (-350, 0)


# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PING PONG GAME")
screen.tracer(0)

r_paddle = Paddle(R_PADDLE_LOCATION)
l_paddle = Paddle(L_PADDLE_LOCATION)

ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Check collision with wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (
        ball.distance(l_paddle) < 50 and ball.xcor() < -320
    ):
        ball.bounce_x()

    # Detect ball miss from the right paddle
    if ball.xcor() > 380:
        ball.reset()
        r_paddle.create_paddle(R_PADDLE_LOCATION)
        l_paddle.create_paddle(L_PADDLE_LOCATION)
        scoreboard.l_point()

    # Detect ball miss from the left paddle
    if ball.xcor() < -380:
        ball.reset()
        r_paddle.create_paddle(R_PADDLE_LOCATION)
        l_paddle.create_paddle(L_PADDLE_LOCATION)
        scoreboard.r_point()


screen.exitonclick()
