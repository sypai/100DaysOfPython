from turtle import Turtle

MOVE_DISTANCE=20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self) -> None:
        self.snake = []
        self.size = 0
        self.manifest()
        self.head = self.snake[0]

    def manifest(self):
        cell = Turtle(shape="square")
        cell.color("#eeeeee")
        cell.pu()
        cell.setpos(0, 0)
        self.snake.append(cell)
        
    def move(self):
        # Moving the body of the snake forward
        for idx in range(self.size - 1, 0, -1):
            curr_cell = self.snake[idx]
            next_cell = self.snake[idx-1]
            curr_cell.goto(next_cell.xcor(), next_cell.ycor())
        
        # Moving the head of the snake forward
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == 270:
            return
        self.head.setheading(UP)

    def down(self):
        if self.head.heading() == 90:
            return
        self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() == 0:
            return
        self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() == 180:
            return
        self.head.setheading(RIGHT)
