from tkinter import *

screen = Tk()
screen.title("My First GUI in py")
screen.minsize(500, 300)


my_label = Label(text="A sample Label", font=("Arial", 24,"bold"))
my_label.pack()


def change_label():
  my_label.config(text=input.get())


button = Button(text="click me", command=change_label)
button.pack()

input = Entry(width=10)
input.pack()


text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of multi-line text entry")
print(text.get("1.0", END))
text.pack()

def spinbox_used():
  print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


def scale_user(value):
  print(value)
scale = Scale(from_=0, to=100, command=scale_user)
scale.pack()


def checkbutton_used():
  print(checked_state.get())


checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()



screen.mainloop()