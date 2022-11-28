from turtle import Turtle, Screen
import time

# Setting the screen up
screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("#222222")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

# Creating the snake body
cells = 2
curr_x = 0
curr_y = 0

snake = []

while cells > 0:
    cell = Turtle(shape="square")
    # t.resizemode("user")
    # t.shapesize(stretch_wid=1, stretch_len=1)
    cell.color("#eeeeee")
    cell.pu()
    cell.setpos(curr_x, curr_y)
    snake.append(cell)
    cells -= 1
    curr_x -= 20

# Snake Movement on user input
user_direction = None # up, down, right, left

# Moving the Snake
game_is_on = True
size = len(snake)

while game_is_on:
    
    screen.update()

    # Moving the body of the snake forward
    for idx in range(size - 1, 0, -1):
        curr_cell = snake[idx]
        next_cell = snake[idx-1]
        curr_cell.goto(next_cell.xcor(), next_cell.ycor())
    
    # Moving the head of the snake forward (or Turning on user input)

    snake[0].fd(20)

    
    time.sleep(0.1)
    


screen.exitonclick()