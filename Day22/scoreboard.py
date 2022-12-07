from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, player_left, player_right):
        super().__init__()
        self.lines()
        self.score_left = 0
        self.score_right = 0
        self.scorecard(player_left, player_right)
        
    def lines(self):
        # Drawing a line, Y-Axis at 0, 0
        # And a circle at center
        self.color("#f2f2f2")
        self.ht()
        self.width(5)
        self.goto(0, -40)
        self.circle(40)
        self.goto(0, -250)
        self.goto(0, 250)
    
    def scorecard(self, player_left, player_right):
        self.pu()
        # Left Player Score
        self.goto(-145, 200)
        self.write(f"{player_left}: {self.score_left}", align="center", font=('Courier', 16, 'normal'))
        
        # Right Player Score
        self.goto(145, 200)
        self.write(f"{player_right}: {self.score_right}", align="center", font=('Courier', 16, 'normal'))
        
    def updateL(self):
        self.score_left += 1
        self.clear()
        self.lines()

    def updateR(self):
        self.score_right += 1
        self.clear()
        self.lines()
