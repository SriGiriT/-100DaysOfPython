from tkinter import *
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

def count_down(count):
  canvas.itemconfig(timer_text, text=count)
  if count>0:
    window.after(1000, count_down, count-1)

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady= 50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg = YELLOW, highlightthickness=0)
label = Label(text= "Timer")
button_to_start = Button(text="Start", highlightthickness=0)
button_to_end = Button(text="Reset", highlightthickness=0)
label.config(font=(FONT_NAME, 40, "bold"), fg=GREEN, bg = YELLOW)
count = Label(text="✓", font=(FONT_NAME, 24, "normal"))
count.config(fg=GREEN, bg = YELLOW)
pomodoro_img = PhotoImage(file="pomodoro-start/tomato.png")
canvas.create_image(100, 112, image=pomodoro_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
button_to_start.grid(row=2, column=0)
button_to_end.grid(row=2, column=2) 
count.grid(row=3, column=1)
window.mainloop()