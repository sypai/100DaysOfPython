from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.listen()

steps = 10
turn_angle = 10
# Event Listeners

def go_forward():
    t.fd(steps)
## Move Forward on 'w'
screen.onkey(key='w', fun=go_forward)

def go_back():
    t.bk(steps)
## Move Backward on 's'
screen.onkey(key='s', fun=go_back)

def turn_anti():
    t.left(turn_angle)
## Move anti-clockwise on 'a'
screen.onkey(key='a', fun=turn_anti)

def turn_clock():
    t.right(turn_angle)
## Move clockwise on 'd'
screen.onkey(key='d', fun=turn_clock)

def erase():
    t.clear()
    t.pu()
    t.home()
    t.pd()

## Move Forward on 'c'
screen.onkey(key='c', fun=erase)

screen.exitonclick()