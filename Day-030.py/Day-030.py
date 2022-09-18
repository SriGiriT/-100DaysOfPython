from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# import pandas
# handling exceptions
# try:
#   file = open("content/new_file.txt")
#   dict_ = {"key":"value"}
#   print(dict_["key"])
# except FileNotFoundError as error_file_not_found:
#   print(error_file_not_found)
#   file = open("content/new_file.txt", "w")
#   file.write("sample")
# except KeyError as key_error:
#   print(key_error)
# else:
#   print(file.read())
# finally:
#   file.close()

# Raise exceptions 
# height = float(input("Enter your height: "))
# weight = int(input("Enter your weight: "))

# if height > 3:
#   raise ValueError("Human height mush be less than 3 meters")

# bmi = weight/height**2
# print(bmi)


# Exception handling in phonetic Day-026.py
# nato_phonetic = pandas.read_csv('content/nato_phonetic_alphabet.csv')
# nato_dict = {row.letter:row.code for (index, row) in nato_phonetic.iterrows()}
# def nato():
#   word = input("Enter a word: ")
#   try: 
#     nato_list = [nato_dict[i] for i in word.upper() ]
#   except KeyError:
#     print("Sorry, only letters in the alphabet please.")
#     nato()
#   else:
#     print(nato_list)

# nato()

def find_password():
  key_website = website_entry.get()
  try:
    with open('content/data.json') as file:
      data = json.load(file)
      try:
        print(data[key_website]['email'], data[key_website]['password'])
      except KeyError:
        messagebox.showinfo(title=key_website, message=f"{key_website} wasn't stored!\nNo details for the website exists")
        password.delete(0, END)
      else:
        messagebox.showinfo(title="password", message=f"Email: {data[key_website]['email']}\nPassword: {data[key_website]['password']}")
        password.delete(0, END)
        password.insert(0, data[key_website]['password'])
        email_entry.delete(0, END)
        email_entry.insert(0, data[key_website]['email'])
        pyperclip.copy(password.get())
  except FileNotFoundError:
    messagebox.showinfo(title="404", message="No Data File Found")
    with open('content/data.json', 'w') as file:
      pass
  except json.JSONDecodeError:
    messagebox.showinfo(title="No Data", message=f"{key_website} wasn't stored!\nNo details for the website exists")
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
  new_dict = {
    webdata:{
      "email":emaildata, 
      "password":passdata
    }
  }
  if len(webdata) <= 0 or len(passdata) <= 0:
    messagebox.showinfo(title="oops...", message="Please make sure you haven't left any fields empty. ")
  else:
    try:
      with open('content/data.json', 'r') as password_file:
        # to write 
        # json.dump(new_dict, password_file, indent= 4)
        # to read the data
        data = json.load(password_file)
        # to update the data
    except json.JSONDecodeError:
      with open('content/data.json', 'w') as password_file:
        json.dump(new_dict, password_file, indent=4)
    except FileNotFoundError:
      with open('content/data.json', 'w') as password_file:
        json.dump(new_dict, password_file, indent=4)
    else:
      data.update(new_dict)
      with open('content/data.json', 'w') as password_file:
        # to write the new data
        json.dump(data, password_file, indent=4)
    finally:
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        email_entry.insert(0, "srigirit369@gmail.com")
        password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="content/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)
website = Label(text="Website:")
email_username = Label(text="Email/Username:")
password_label = Label(text="Password:")
website_entry = Entry(width=24)
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
website_entry.grid(column=1, row=1)
email_entry.grid(column=1, row=2, columnspan=2)
generate_password.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", padx=0, pady=0,width=16, command=find_password)
search_button.grid(column=2, row = 1)

window.mainloop()


