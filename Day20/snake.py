from turtle import Turtle

MOVE_DISTANCE=20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self) -> None:
        self.snake = []
        self.manifest((0, 0))
        self.head = self.snake[0]

    def manifest(self, position):
        if len(self.snake) < 1:
            cell = Turtle(shape="triangle")
            cell.color("#F0E68C")
        else:
            cell = Turtle(shape="square")
            cell.color("#eeeeee")    
        cell.pu()
        cell.goto(position)
        self.snake.append(cell)

    def grow(self):
        self.manifest(self.snake[-1].position())

    def move(self):
        # Moving the body of the snake forward

        # OKAY...Here is the problem. Found it! Silly
        # self.size gets set to 0 during construction
        # and never gets updated
        # Thus this for loop never runs
        # resulting in no movement of added segments while head keeps going forward
        # for idx in range(self.size - 1, 0, -1):
        for idx in range(len(self.snake) - 1, 0, -1):
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
