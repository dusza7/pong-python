from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, l_score, r_score):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.update_scoreboard(l_score, r_score)

    def update_scoreboard(self, l_score, r_score):
        self.clear()
        self.goto(-100, 250)
        self.write(l_score, align="center", font=("Courier", 30, "normal"))
        self.goto(100, 250)
        self.write(r_score, align="center", font=("Courier", 30, "normal"))