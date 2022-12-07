from turtle import Screen
from player import Player, ScoreBoard
from cars import Car
import time

# Setting the screen up
X = 600
Y = 600
screen = Screen()
screen.setup(width=X, height=Y)
screen.title("Cross the road!")
screen.bgcolor("#F0FFFF")
screen.tracer(0)
screen.colormode(255)

p = Player()
s = ScoreBoard()
c = Car()

# Player Movement
screen.listen()
screen.onkeypress(fun=p.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    c.live()
    c.move_cars()

    # Detect collision with car
    for car in c.cars:
        if car.distance(p) < 20:
            game_is_on = False

    # Detect if Turtle reaches Finish line
    if p.ycor() > 240:
        s.level_up()
        p.level_up()
        c.level_up()

screen.exitonclick()