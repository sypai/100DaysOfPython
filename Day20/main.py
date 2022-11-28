from turtle import Turtle, Screen
from snake import Snake
import time

# Setting the screen up
screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("#222222")
screen.title("Snake Game")
screen.tracer(0)


s = Snake()


# Game Engine
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    s.move()

    # Snake Movement on user input
    screen.listen()
    screen.onkey(fun=s.up, key="Up")
    screen.onkey(fun=s.down, key="Down")    
    screen.onkey(fun=s.left, key="Left")
    screen.onkey(fun=s.right, key="Right")


screen.exitonclick()