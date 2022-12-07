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
        # self.speed(1)
        self.shape("circle")
        self.loc = [0, 0]
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.07

    def move(self):
        self.goto(self.loc[0], self.loc[1])

    def play(self):
        self.loc[0] += self.x_move
        self.loc[1] += self.y_move
        self.move()

    def bounceY(self):
        self.y_move *= -1
        self.move_speed *= 0.5

    def bounceX(self):
        self.x_move *= -1
        self.move_speed *= 0.5

    def restart(self):
        self.loc = [0, 0]
        self.bounceX()
        self.play()
        