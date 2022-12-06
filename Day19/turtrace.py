from turtle import Turtle, Screen
import random

# Setting the screen
screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("#E6E6FA")
screen.title("Welcome to Turtle Racing")
user_bet = screen.textinput("Turtle Racing: VIBGYexiOR", "Which color are you placing your bet on?")

turtles = []
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

x = -580
y = 175 
# Turtle Initiation
for _ in range(7):
    t = Turtle(shape="turtle")
    t.turtlesize(2, 2, 1)
    t.color(colors[_])
    t.pu()
    t.goto(x, y)
    y -= 50
    turtles.append(t)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in turtles:
        step_size = random.randrange(-30, 60)
        turtle.fd(step_size)
        curr_x = turtle.xcor()
        if curr_x >= 580:
            curr_color = turtle.pencolor()
            if curr_color == user_bet:
                print("Yes! Your turtle won!")
            else:
                print(f"And! {curr_color} won!")
            is_race_on = False

screen.exitonclick()
