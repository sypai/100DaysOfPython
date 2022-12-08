from turtle import Screen
from snake import Snake
from food import Food
from score import Score, Box
import time

# Setting the screen up
screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("#222222")
screen.title("Snake Game")
screen.tracer(0)

s = Snake()
f = Food()
txt = Score()
box = Box()

# Snake Movement on user input
screen.listen()
screen.onkey(fun=s.up, key="Up")
screen.onkey(fun=s.down, key="Down")    
screen.onkey(fun=s.left, key="Left")
screen.onkey(fun=s.right, key="Right")

# Game Engine
# time.sleep(2)
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    s.move()

    # Detect snake's collision with food
    if s.head.distance(f) < 15:
        f.refresh()
        txt.update()
        s.grow()

    # Detect snake's collision with the wall
    if s.head.xcor() > 320 or s.head.xcor() < -320 or s.head.ycor() > 320 or s.head.ycor() < -320:
        txt.game_over()
        txt.high_scored()
        game_is_on = False
    
    # Detect snake's collision with itself
    for cell in s.snake:
        if len(s.snake) < 3:
            break
        if cell == s.head:
            pass
        elif s.head.distance(cell) < 10:
            txt.game_over()
            txt.high_scored()
            game_is_on = False

screen.exitonclick()