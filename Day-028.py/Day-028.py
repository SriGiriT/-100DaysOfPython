from tkinter import *
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
SEC = 60

reps = 0
timer = None

def reset():
  global reps
  reps = 0
  window.after_cancel(timer)
  label.config(text="Timer", fg=GREEN)
  canvas.itemconfig(timer_text, text="00:00")
  sessions.config(text="")


def start_timer():
  work_time_sec = WORK_MIN * SEC
  short_break_sec = SHORT_BREAK_MIN * SEC
  long_break_sec = LONG_BREAK_MIN * SEC
  global reps
  reps += 1
  if reps % 8 == 0:
    count_down(long_break_sec)
    label.config(text="Break", fg=RED)
  elif reps % 2 == 0: 
    count_down(short_break_sec)
    label.config(text="Break", fg=PINK)
  else:
    count_down(work_time_sec)
    label.config(text="Work", fg=GREEN)

def count_down(count):
  count_min = count // SEC
  count_sec = count % SEC
  if count_min <= 9:
    count_min = "0"+str(count_min)
  if count_sec<=9:
    count_sec="0"+str(count_sec)
  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  if count>0:
    global timer
    timer = window.after(1000, count_down, count-1)
  else:
    start_timer()
    work_sessions = reps//2
    marks = ""
    for _ in range(work_sessions):
      marks+="✓"
    sessions.config(text=marks)


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady= 50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg = YELLOW, highlightthickness=0)
label = Label(text= "Timer")
button_to_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_to_end = Button(text="Reset", highlightthickness=0, command=reset)
label.config(font=(FONT_NAME, 40, "bold"), fg=GREEN, bg = YELLOW)
sessions = Label(font=(FONT_NAME, 24, "normal"))
sessions.config(fg=GREEN, bg = YELLOW)
pomodoro_img = PhotoImage(file="pomodoro-start/tomato.png")
canvas.create_image(100, 112, image=pomodoro_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
button_to_start.grid(row=2, column=0)
button_to_end.grid(row=2, column=2) 
sessions.grid(row=3, column=1)
window.mainloop()