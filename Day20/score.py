from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.read_high_score()
        super().__init__()
        self.hideturtle()
        self.color("#eeeeee")
        self.pu()
        self.goto(-175, 324)
        self.write("SCORE: 0", align="center", font=('Courier', 16, 'bold'))
        self.goto(175, 324)
        self.write(f"HIGH SCORE: {self.high_score}", align="center", font=('Courier', 16, 'bold'))

    def read_high_score(self):
        with open("data.txt") as file:
            score = int(file.read())
            self.high_score = score

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Courier', 16, 'bold'))

    def update(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.clear()
        self.goto(-175, 324)
        self.write(f"SCORE: {self.score}", align="center", font=('Courier', 16, 'bold'))
        self.goto(175, 324)
        self.write(f"HIGH SCORE: {self.high_score}", align="center", font=('Courier', 16, 'bold'))
        self.update_high_score_in_file()

    def update_high_score_in_file(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def high_scored(self):
        self.goto(0, 30)
        self.write(f"WOW! This is a new High Score!", align="center", font=('Courier', 16, 'bold'))

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