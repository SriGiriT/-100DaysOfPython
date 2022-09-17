from tkinter import *
from tkinter import messagebox
import random
import pyperclip

def print_passwords():
  with open('saved_password.txt') as passwords:
    data = passwords.readlines()
    for i in data:
      print(i.split(" | "))
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password_():
  password.delete(0, END)
  length = random.randint(8, 10)
  len_symbols = random.randint(2, 4)
  len_numbers = random.randint(2, 4)
  alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  digits = "0123456789"
  symbol = "\"\'\\/!@#$%^&*()_+-={}[]|:;<>,.`~"
  list_answer =  [alpha[random.randint(0, len(alpha)-1)] for _ in range(length)]
  list_answer.extend(digits[random.randint(0, len(digits)-1)] for _ in range(len_numbers))
  list_answer.extend(symbol[random.randint(0, len(symbol)-1)] for _ in range(len_symbols))
  random.shuffle(list_answer)
  password_generated = "".join(list_answer)
  password.insert(0, password_generated)
  pyperclip.copy(password_generated)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
  webdata = website_entry.get().strip()
  emaildata = email_entry.get().strip()
  passdata = password.get().strip()
  if len(webdata) <= 0 or len(passdata) <= 0:
    messagebox.showinfo(title="oops...", message="Please make sure you haven't left any fields empty. ")
  else:
    is_ok = messagebox.askokcancel(title=webdata, message=f"These are the details entered: \nEmail: {emaildata} \nPassword: {passdata} \nIs it ok to save?")
    if is_ok:
      with open('saved_password.txt', 'a') as password_file:
        password_file.write(f"{webdata} | {emaildata} | {passdata}\n")
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        email_entry.insert(0, "srigirit369@gmail.com")
        password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="password-manager-start/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)
website = Label(text="Website:")
email_username = Label(text="Email/Username:")
password_label = Label(text="Password:")
website_entry = Entry(width=40)
email_entry = Entry(width=40)
password = Entry(width=24)
website_entry.focus()
email_entry.insert(0, "srigirit369@gmail.com")
generate_password = Button(text="Generate Password", padx=0, pady=0, command=generate_password_)
add_button = Button(text="Add",width=40, padx=0,pady=0,command=save_password)
website.grid(column=0, row=1)
email_username.grid(column=0, row=2)
password_label.grid(column=0, row=3)
password.grid(column=1, row=3)
website_entry.grid(column=1, row=1, columnspan=2)
email_entry.grid(column=1, row=2, columnspan=2)
generate_password.grid(column=1, row=3)
generate_password.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)
show_passwords = Button(text="show", width=40, command=print_passwords, padx=0, pady=0)
show_passwords.grid(column=1, row=5, columnspan=2)

window.mainloop()


