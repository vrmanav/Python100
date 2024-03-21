import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

FINISH_LINE_Y = 293

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Check detection with upper wall
    if player.ycor() >= FINISH_LINE_Y:
        scoreboard.increase_score()
        player.start()
        car_manager.increase_speed()

    # Check for game over
    for car in car_manager.cars:
        if player.distance(car) < 21:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
