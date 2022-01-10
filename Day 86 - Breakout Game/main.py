from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from targets import Target
from lives import Lives
import time
import random

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -260))

ball = Ball((0, -230))

lives = Lives()

screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")

tx, ty = -250, 280
dy = 1
dx = random.choice([-.5, .5])
targets = []
for x in range(5):
    for y in range(10):
        target = Target(tx, ty)
        targets.append(target)
        tx += 55
    ty -= 25
    tx = -250

game_is_on = True
while game_is_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.vertical_bounce()

    if ball.ycor() > 270:
        ball.horizontal_bounce()

    if ball.distance(paddle) < 50 and ball.ycor() < -230:
        ball.horizontal_bounce()

    if ball.ycor() < -280:
        ball.reset()
        lives.live()
        if lives.lives == 0:
            lives.game_over()
            game_is_on = False

    for x in targets:
        if ball.distance(x) < 30:
            ball.vertical_bounce()
            x.goto(2500,2500)
            targets.remove(x)

screen.exitonclick()
