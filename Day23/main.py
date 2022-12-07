from turtle import Screen
from player import Player, ScoreBoard
import time

# Setting the screen up
X = 600
Y = 600
screen = Screen()
screen.setup(width=X, height=Y)
screen.title("Cross the road!")
screen.bgcolor("#F0FFFF")
screen.tracer(0)

p = Player()
s = ScoreBoard()

# Player Movement
screen.listen()
screen.onkeypress(fun=p.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()