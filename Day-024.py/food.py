from random import randint
from turtle import Turtle



class Food(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.shapesize(stretch_len=0.5, stretch_wid=0.5)
    self.penup()
    self.speed("fastest")
    self.color("blue")
    self.refresh()


  def refresh(self):
    self.goto(randint(-280, 280), randint(-280, 280))
