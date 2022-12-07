from turtle import Turtle
import random
import time

class Car():
    def __init__(self):
        self.cars = []
        self.level = 10

    def live(self): 
        num = random.randint(1, self.level)
        if num == 1:
            y_cor = random.randrange(-235, 245)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            # Create a Car
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(r, g, b)
            car.pu()
            car.goto(320, y_cor)
            
            self.cars.append(car)

    def level_up(self):
        self.level -= 1


    def move_cars(self):
        for car in self.cars:
            car.backward(50/self.level)
            
    
            
            


