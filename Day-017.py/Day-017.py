from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
  question = Question(i['question'], i['correct_answer'])
  question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
  quiz.ask_question()


print("You completed the quiz...")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")