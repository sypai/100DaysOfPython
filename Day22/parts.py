from turtle import Turtle

class Bat(Turtle):
    def __init__(self, X, Y):
        super().__init__()
        self.pu()
        self.color("#f2f2f2")
        self.speed(0)
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=4)
        self.loc = [X, Y]
        self.move()

    def move(self):
        self.goto(self.loc[0], self.loc[1])
  
    def up(self):
        self.loc[1] += 20
        self.move()

    def down(self):
        self.loc[1] -= 20
        self.move()

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color("#f2f2f2")
        self.speed(1)
        self.shape("circle")
        self.loc = [0, 0]
        self.virginity = True
        self.direction = True # T for Up, F for Down

    def move(self):
        self.goto(self.loc[0], self.loc[1])

    def play(self):
        if self.virginity: # To start the game, balls goes +x, +y
            self.loc[0] += 10
            self.loc[1] += 10

        elif self.direction: 
            self.loc[0] += 10
            self.loc[1] -= 10
        else: 
            self.loc[0] += 10
            self.loc[1] += 10
        self.move()

    def bounce(self, side):
        if side == "+":
            self.virginity = True
            self.move()
        