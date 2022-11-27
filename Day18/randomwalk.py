from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()

directions = [0, 90, 180, 270]
steps = 30
t.speed(0)
t.width(10)

screen.colormode(255)

for _ in range(1000):
    t.fd(steps)
    t.setheading(random.choice(directions))
    t.pencolor(random.randrange(255), random.randrange(255), random.randrange(255))

screen.exitonclick()

