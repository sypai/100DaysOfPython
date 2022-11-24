from turtle import Turtle, Screen
import random

t = Turtle()
# t.speed(2)
t.width(2)

screen = Screen()
screen.colormode(255)
# screen.bgcolor("#111111")

# Edge length
a = 50

# Trying to draw a Triangle

# t.pencolor("#F0F8FF")
# t.setx(-a)
# t.setx(a)
# t.right(120)
# t.fd(2*a)
# t.right(120)
# t.fd(2*a)
# t.pencolor("#F0F8FF")

# Making polygons 
n = 3

t.setx(-a)
t.setx(a)

while n < 10:

    t.pencolor(random.randrange(50), random.randrange(255), random.randrange(120))
    angle = 360 / n

    for _ in range(n):
        t.left(angle)
        t.fd(2*a)
    
    for _ in range(n):
        t.right(angle)
        t.fd(2*a)
    
    n += 1
    

screen.exitonclick()