from turtle import Turtle 


class Score(Turtle):
  def __init__(self):
    self.score = 0
    super().__init__()
    self.penup()
    self.color("white")
    self.hideturtle()
    self.goto(0, 270)
    self.display()


  def display(self):
    self.write(f"Score : {self.score}", False, "center", ("Courier", 18, "normal"))

  def game_over(self):
    self.goto(0, 0)
    self.write("GAME OVER", False, "center", ("Courier", 24, "normal"))

  def addScore(self):
    self.score+=1;
    self.clear()
    self.display()

  def reset_score(self):
    self.clear()
    self.score = 0