import time
from scoreboard import Scoreboard
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
l_score = 0
r_score = 0

scoreboard = Scoreboard(l_score, r_score)
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

ball = Ball()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    ball.move()
    ball.collision()
    screen.update()

    #detect coll with r_paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor()) > 320 or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce()

    if ball.l_reset():
        r_score += 1

    if ball.r_reset():
        l_score += 1

    scoreboard.update_scoreboard(l_score, r_score)



screen.exitonclick()
