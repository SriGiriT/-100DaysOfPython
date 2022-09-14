from tkinter import *

def calculate():
  label_value.config(text=str(int(int(entry.get())*1.609)))
# alter 
def miles_to_km():
  miles = float(entry.get())
  km = round(miles*1.609)
  label_value.config(text=f"{km} ")
screen = Tk()
screen.minsize(width=400, height=300)
screen.config(padx=200, pady=200)
screen.title("Mile to Km Converter")
entry = Entry()
entry.grid(column=2, row=1)
label_miles = Label(text="Miles")
label_miles.grid(column=3, row=1)
label_is_equal_to = Label(text="is equal to")
label_is_equal_to.grid(column=1, row=2)
label_value = Label(text="0")
label_value.grid(column=2, row=2)
label_km = Label(text="Km")
label_km.grid(column=3, row=2)
button = Button(text="Calculate", command=calculate)
button.grid(column=2, row=3)





screen.mainloop()