from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.setheading(90)
        self.pu()
        self.goto(0, -270)
        self.steps = 10
        
    def move(self):
        self.fd(self.steps)

    def level_up(self):
        self.goto(0, -270)
    

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.points = 1
        self.score()
        self.draw_track()
    
    def score(self):
        self.pu()
        self.goto(230, 270)
        self.write(f"Level: {self.points}", align="center", font=('Courier', 16, 'normal', 'bold'))

    def draw_track(self):
        # Start Line
        self.goto(-300, -270)
        self.pd()
        self.goto(200, -270)
        self.pu()
        self.goto(235, -270)
        self.write("START", align="center", font=('Courier', 18, 'normal'))
        self.goto(260, -270)
        self.pd()
        self.goto(300, -270)

        # End Line
        self.pu()
        self.goto(-300, 250)
        self.pd()
        self.goto(-270, 250)
        self.pu()
        self.goto(-235, 250)
        self.write("FINISH", align="center", font=('Courier', 18, 'normal'))
        self.goto(-200, 250)
        self.pd()
        self.goto(300, 250)

    def level_up(self):
        self.points += 1
        self.clear()
        self.draw_track()
        self.score()

    def game_over(self):
        self.pu()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Courier', 28, 'bold'))
    
