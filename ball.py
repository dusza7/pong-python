from turtle import Turtle

UP = 90
DOWN = 270


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.goto(0, 0)
        self.setheading(45)
        speed = 0

    def move(self):
        # new_y = self.ycor() + 1
        # new_x = self.xcor() + 1
        self.forward(5)

    def collision(self):
        if self.ycor() > 291 or self.ycor() < -291:
            self.bounce()

    def bounce(self):
        print(self.heading())
        new_heading = self.heading() + 90
        self.setheading(new_heading)
        print(self.heading())

    def l_reset(self):
        if self.xcor() < -395:
            self.goto(0, 0)
            return 1

    def r_reset(self):
        if self.xcor() > 395:
            self.goto(0, 0)
            return 1
