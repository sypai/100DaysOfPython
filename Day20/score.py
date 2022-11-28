from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.hideturtle()
        self.color("#eeeeee")
        self.pu()
        self.goto(0, 324)
        self.write("SCORE: 0", align="center", font=('Courier', 16, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Courier', 16, 'bold'))


    def update(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE: {self.score}", align="center", font=('Courier', 16, 'bold'))


class Box(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.boundary()

    def boundary(self):
        self.color("#eeeeee")
        self.width(2)
        self.goto(-320, 320)
        self.pd()
        self.goto(320, 320)
        self.goto(320, -320)
        self.goto(-320, -320)
        self.goto(-320, 320)