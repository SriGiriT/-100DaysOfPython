# import smtplib

# with smtplib.SMTP("smtp.gmail.com") as connection:
#   connection.starttls()
#   connection.login(user="tsrigiri369@gmail.com", password="fqdnktfvpxzlsmtw")
#   connection.sendmail(from_addr="tsrigiri369@gmail.com", to_addrs="srigirit369@gmail.com", msg="Subject: Test email\n\nThis was just a test email")

# monday motivation 
# import random 
# import datetime as dt
# import smtplib

# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 1:
#   with open('content/quotes.txt') as file:
#     all_quotes = file.readlines()
#     quotes = random.choice(all_quotes)

#   with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user="tsrigiri369@gmail.com", password="fqdnktfvpxzlsmtw")
#     connection.sendmail(from_addr="tsrigiri369@gmail.com", to_addrs="srigirit369@gmail.com", msg=f"Subject: Monday Motivation \n\n{quotes}")

# Day-032.py final proj
import smtplib
import random 
import datetime as dt 
import pandas

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv('content/birthdays.csv')
birthday_dict = {(data_row['month'], data_row['day']):data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
  birthday_person = birthday_dict[today_tuple]
  file_path = f"content/letter_templates/letter_{random.randint(1, 3)}.txt"
  with open(file_path) as file:
    content = file.read()
    content = content.replace("[NAME]", birthday_person["name"])
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user="tsrigiri369@gmail.com", password="fqdnktfvpxzlsmtw")
    connection.sendmail(from_addr="tsrigiri369@gmail.com", to_addrs="srigirit369@gmail.com", msg=f"Subject: Happy Birthday!!! \n\n{content}")