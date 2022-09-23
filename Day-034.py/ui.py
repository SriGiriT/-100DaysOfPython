from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
  def __init__(self, quiz_brain:QuizBrain):
    self.quiz = quiz_brain
    self.score = 0
    self.window = Tk()
    self.window.title("Quizzler")
    self.canvas = Canvas(width=300, height=250, highlightthickness=0)
    self.question_to_display = self.canvas.create_text(150, 125, text=f"a sample question will occupies this space and this was the question to ask the user for the answer True/False", fill=THEME_COLOR, font=("Arial", 14, "italic"), width=200)
    self.label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
    wrong_img = PhotoImage(file="images/false.png")
    right_img = PhotoImage(file="images/true.png")
    self.wrong_button = Button(image=wrong_img, command=self.true_pressed)
    self.right_button = Button(image=right_img, command=self.false_pressed)
    self.window.config(padx=20, pady=20, bg=THEME_COLOR)
    self.label.grid(row=0, column=1)
    self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
    self.wrong_button.grid(row=2, column=1)
    self.right_button.grid(row=2, column=0)
    self.get_next_question()
    self.window.mainloop()

  def get_next_question(self):
    self.canvas.config(bg="white")
    self.label.config(text = f"Score: {self.quiz.score}")
    q_text = self.quiz.next_question()
    self.canvas.itemconfig(self.question_to_display, text=q_text)

  def true_pressed(self):
    self.feedback(self.quiz.check_answer("True"))
  def false_pressed(self):
    self.feedback(self.quiz.check_answer("False"))

  def feedback(self, is_right):
    if is_right:
      self.canvas.config(bg="green")
    else:
      self.canvas.config(bg="red")
    self.window.after(1000, self.get_next_question)
