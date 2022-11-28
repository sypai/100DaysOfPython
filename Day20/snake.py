from turtle import Turtle

class Snake:
    def __init__(self) -> None:
        self.snake = []
        self.size = 0
        self.manifest()

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
        
        # Moving the head of the snake forward (or Turning on user input)
        self.snake[0].fd(20)