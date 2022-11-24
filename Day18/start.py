from turtle import Turtle, Screen

t = Turtle()

t.width(5)

# Making a square
# I want it's center to be at 0, 0
# A(-100, 100), B(100, 100), C(100, -100), D(-100, -100)
t.penup()
t.setx(100)
t.sety(100)
t.pendown()

t.speed(1)
t.sety(-100)
t.setx(-100)
t.sety(100)
t.setx(100)

# Drawing a dashed line
# instead I'll draw dashed diagonals

# Drawing BD without dashing
# t.goto(-100, -100)
x = 100
y = 100
while x > -100:
    t.pd()
    x -= 10
    y -= 10
    t.goto(x, y)
    t.pu()
    x -= 10
    y -= 10
    t.goto(x, y)

t.goto(-100, 100)
# Drawing AC
x = -100
y = 100
while x < 100:
    t.pd()
    x += 10
    y -= 10
    t.goto(x, y)
    t.pu()
    x += 10
    y -= 10
    t.goto(x, y)

screen = Screen()
screen.exitonclick()

