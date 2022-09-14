from tkinter import *


def add(*args):
  return sum(args)

print(add(10, 20, 30, 40, 50, 60, 70, 80, 90, 100))


def calculate(n, **kwargs):
  n += kwargs["add"]
  n *= kwargs["multiply"]
  return n

print(calculate(2, add=3, multiply=5))


# all about tkinter
# screen = Tk()
# screen.title("My First GUI in py")
# screen.minsize(500, 300)


# my_label = Label(text="A sample Label", font=("Arial", 24,"bold"))
# my_label.pack()


# def change_label():
#   my_label.config(text=input.get())


# button = Button(text="click me", command=change_label)
# button.pack()

# input = Entry(width=10)
# input.pack()


# text = Text(height=5, width=30)
# text.focus()
# text.insert(END, "Example of multi-line text entry")
# print(text.get("1.0", END))
# text.pack()

# def spinbox_used():
#   print(spinbox.get())


# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()


# def scale_user(value):
#   print(value)
# scale = Scale(from_=0, to=100, command=scale_user)
# scale.pack()


# def checkbutton_used():
#   print(checked_state.get())


# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()


# def radio_used():
#   print(radio_state.get())

# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()

# def listbox_used(event):
#   print(listbox.get(listbox.curselection()))

# listbox = Listbox(height=4)
# fruits = ["apple", "pear", "orange", "banana"]
# for i in fruits:
#   listbox.insert(fruits.index(i), i)

# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# screen.mainloop()

# Layout manager 
# pack 
# just pack the widget at top, bottom , left or right 

screen = Tk()
screen.title("Day-027.py")
screen.config(padx=100, pady=200 )
screen.minsize(width=500, height=300)
label = Label(text="Label", font=("Arial", 24, "bold"))
label.config(text="New Text")
label.config(padx=50, pady=50)
# label.pack()


# place 
# place the widget at precise position 
# label.place(x=100, y=200)

# grid 
# we are gone consider our screen as grid and work according to that 
label.grid(column=1, row=1)
button = Button(text="button")
button.grid(column=2, row=2)
button1 = Button(text="new button")
button1.grid(column=3, row=1)
entry = Entry()
entry.grid(column=4, row=4)
# padding 
# at line 81 and 85 ( for specific padding for a widget )
screen.mainloop()