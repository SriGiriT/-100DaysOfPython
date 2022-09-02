from turtle import Screen, Turtle
from time import sleep 
from snake import Snake


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("MY Snake Game")

screen.tracer(0)
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right , "Right")

is_game_on = True
while is_game_on:
  screen.update()
  sleep(0.1)
  snake.move()





screen.exitonclick()