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
    position = [(0,0), (0, -20), (0, -40)]
    for i in position:
      self.add_segment(i)


  def add_segment(self, i):
      newSegment = Turtle("square")
      newSegment.color("white")
      newSegment.penup()
      newSegment.goto(i)
      self.snake.append(newSegment)
  
  def extend(self):
    self.add_segment(self.snake[-1].position())

  def move(self):
    for i in range(len(self.snake)-1, 0, -1):
      x_pos = self.snake[i-1].xcor()
      y_pos = self.snake[i-1].ycor()
      self.snake[i].goto(x_pos, y_pos)
    self.head.fd(20)


  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)

  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)


  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)

  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)