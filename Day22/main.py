from turtle import Screen
from parts import Bat, Ball
from scoreboard import ScoreBoard
import time

# Setting the screen up
X = 740
Y = 480
screen = Screen()
screen.setup(width=X, height=Y)
screen.bgcolor("#111111")
screen.title("Arcade")
screen.tracer(0)

nameL = screen.textinput("And the fun begins!", "What's your name buddy? \nRemember! 'w' moves your bat up & 's' slides it down!" )
nameR = screen.textinput("And the fun begins!", f"Who is playing against {nameL}? \nYou will use the arrows 'Up' and 'Down' to move...")

# Paddles
x = (X/2) - 20
p1 = Bat(x, 0)
p2 = Bat(-x-5, 0)

# Ball
b = Ball()

# Scoreboard
s = ScoreBoard(nameL, nameR)

screen.listen()
screen.onkeypress(fun=p1.up, key="Up")
screen.onkeypress(fun=p1.down, key="Down")
screen.onkeypress(fun=p2.up, key="w")
screen.onkeypress(fun=p2.down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(b.move_speed)
    screen.update()

    b.play()
    s.scorecard(nameL, nameR)

    # Detecting a collision with the borders UP and DOWN (ball bounce)
    if b.ycor() > 220  or b.ycor() < -220:
        b.bounceY()

    # Detecting a collision with the right paddle
    if b.xcor() > 320 and (b.ycor() < p1.ycor() + 40 and b.ycor() > p1.ycor() - 40):
        b.bounceX()
    elif b.xcor() > 360:
        s.updateL()
        s.scorecard(nameL, nameR)
        b.restart()

    # Detecting a collision with the left paddle
    if b.xcor() < -320 and (b.ycor() < p2.ycor() + 40 and b.ycor() > p2.ycor() - 40):
        b.bounceX()
    elif b.xcor() < -360:
        s.updateR()
        s.scorecard(nameL, nameR)
        b.restart()

screen.exitonclick()