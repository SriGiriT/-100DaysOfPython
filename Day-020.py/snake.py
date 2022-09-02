from os import popen
from turtle import Screen, Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  def __init__(self) -> None:
    self.snake = []
    self.create_snake()
    self.head = self.snake[0]

  def create_snake(self):
    position = [0, 0]
    for i in range(3):
      self.snake.append(Turtle("square"))
      self.snake[i].color("white")
      self.snake[i].penup()
      self.snake[i].goto(x=position[0], y=position[1])
      position[0] -= 20
  

  def move(self):
    for i in range(len(self.snake)-1, 0, -1):
      x_pos = self.snake[i-1].xcor()
      y_pos = self.snake[i-1].ycor()
      self.snake[i].goto(x_pos, y_pos)
    self.head.fd(20)


  def up(self):
    if self.head.heading() != UP:
      self.head.setheading(UP)

  def down(self):
    if self.head.heading() != DOWN:
      self.head.setheading(DOWN)


  def left(self):
    if self.head.heading() != LEFT:
      self.head.setheading(LEFT)

  def right(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(RIGHT)