from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()


t.speed(0)
# t.width(2)

screen.colormode(255)

for _ in range(0, 360, 5):
    t.circle(100)
    t.setheading(_)
    t.pencolor(random.randrange(255), random.randrange(255), random.randrange(255))

screen.exitonclick()
