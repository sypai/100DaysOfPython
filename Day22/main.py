from turtle import Turtle, Screen
from parts import Bat, Ball
import time

# Setting the screen up
X = 740
Y = 480
screen = Screen()
screen.setup(width=X, height=Y)
screen.bgcolor("#111111")
screen.title("Arcade")
screen.tracer(0)

# Paddles
x = (X/2) - 20
p1 = Bat(x, 0)
p2 = Bat(-x-5, 0)

# Ball
b = Ball()

screen.listen()
screen.onkeypress(fun=p1.up, key="Up")
screen.onkeypress(fun=p1.down, key="Down")
screen.onkeypress(fun=p2.up, key="w")
screen.onkeypress(fun=p2.down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    b.play()

    # Detecting a collision with the borders UP and DOWN (ball bounce)
    if b.ycor() > Y/2-10:
        b.bounce(side="+")
    elif b.ycor() > -(Y/2-20):
        b.bounce(side="-")

    # Detecting a collision with the paddle

screen.exitonclick()