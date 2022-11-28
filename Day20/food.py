from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.color("#ADFF2F")
        self.refresh()
        
    def refresh(self):
        random_x = random.randrange(-300, 300)
        random_y = random.randrange(-300, 300)
        self.goto(random_x, random_y)
        