from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()
screen.update()
screen.listen()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

is_game_on = True
ball.move()
while is_game_on:
  screen.update()
  ball.move()
  sleep(0.1)
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.y_bounce()

  if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
    ball.x_bounce()
    

  if ball.xcor() > 380:
    ball.reset_position()
    score.l_point()

  if ball.xcor() < -380:
    ball.reset_position()
    score.r_point()








screen.exitonclick()