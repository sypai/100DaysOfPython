from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.speed("fastest")
        self.color("#ADFF2F")
        random_x = random.randrange(-320, 320)
        random_y = random.randrange(-320, 320)
        self.goto(random_x, random_y)
        
