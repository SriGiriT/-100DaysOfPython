import html


class QuizBrain:
  

  def __init__(self, question_bank):
    self.question_number = 0
    self.question_bank = question_bank
    self.score = 0


  def ask_question(self):
    text = html.unescape(self.question_bank[self.question_number].text)
    answer = input(f"Q.{self.question_number+1}: {text}. (True/False) ")
    self.check_answer(answer, self.question_bank[self.question_number].answer)
    self.question_number += 1


  def still_has_question(self):
    return self.question_number < len(self.question_bank)


  def check_answer(self, user_answer, correct_answer):
    if(user_answer.lower() == correct_answer.lower()):
      print("You got it right!!!")
      self.score += 1
    else:
      print("You are wrong")
    print(f"The correct answer is {correct_answer}")
    print(f"Your score: {self.score}/{self.question_number+1}\n")




