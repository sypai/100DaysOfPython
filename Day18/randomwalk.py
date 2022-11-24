from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()

directions = [0, 90, 180, 270]
steps = 60
t.speed(0)
t.width(15)

screen.colormode(255)

for _ in range(100):
    t.fd(steps)
    t.setheading(random.choice(directions))
    t.pencolor(random.randrange(255), random.randrange(255), random.randrange(255))

screen.exitonclick()

