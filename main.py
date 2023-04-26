from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

player1 = Paddle(-350)
player2 = Paddle(350)
ball = Ball()
score = Scoreboard()

screen.listen()

screen.onkey(player1.go_up, "w")
screen.onkey(player1.go_down, "s")

screen.onkey(player2.go_up, "i")
screen.onkey(player2.go_down, "k")

game_is_on = True

while game_is_on:
    time.sleep(ball.moove_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(player2) < 50 and ball.xcor() > 320 or ball.distance(player1) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()