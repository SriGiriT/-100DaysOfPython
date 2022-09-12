import tkinter

screen = tkinter.Tk()
screen.title("My First GUI in py")
screen.minsize(500, 300)


my_label = tkinter.Label(text="A sample Label", font=("Arial", 24,"bold"))
my_label.pack(expand=True)






screen.mainloop()