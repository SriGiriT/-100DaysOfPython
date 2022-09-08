from turtle import Turtle 


class Score(Turtle):
  def __init__(self):
    self.score = 0
    with open("score.txt") as file:
      score_from_text = file.read()
    self.high_score = int(score_from_text)
    super().__init__()
    self.penup()
    self.color("white")
    self.hideturtle()
    self.goto(0, 270)
    self.display()


  def display(self):
    self.clear()
    self.write(f"Score : {self.score} High Score : {self.high_score}", False, "center", ("Courier", 18, "normal"))

  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
    with open("score.txt", "w") as file:
      file.write(str(self.high_score))
    self.score = 0
    self.display()

  def addScore(self):
    self.score+=1
    self.display()

  def reset_score(self):
    self.clear()
    self.score = 0