import csv
import pandas
import turtle
# names = []
# with open('weather_data .csv') as file:
#   data = file.readlines()
#   for line in data:
#     names.append(line.strip())
# print(names)

# with open('weather_data .csv') as file:
#   data = csv.reader(file)
#   temperatures  = []
#   for row in data:
#     print(row)
#     if row[1] != "temp":
#       temperatures.append(int(row[1]))
#   print(temperatures)


# data = pandas.read_csv("weather_data .csv")
# print(type(data))          # DataFrame
# print(type(data['temp']))  # Series


# temp_dict = data.to_dict()
# print(temp_dict)

# temp_list = data['temp'].tolist()
# print(temp_list)

# print("Average temperature", sum(temp_list)/len(temp_list))
# # with pandas
# print("Average temperature", data["temp"].mean())

# print("Maximum value of temperature", data["temp"].max())

# # get data in columns 
# print(data["condition"])
# print(data.condition)

# # get data in row 
# print(data[data.day == "Monday"])
# # print the maximum data row 
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# temp = int(monday.temp) * 9/5 + 32
# print(temp)

# create own data_frame 
# data_dict = {
#   "students" : ["raja", "ramesh", "varun"],
#   "scores" : [76, 98, 100]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_csv.csv")

# data = pandas.read_csv("Squirrel_Data.csv")
# lis = []
# for i in data["Primary Fur Color"]:
#   if i not in lis:
#     lis.append(i)

# for i in lis:
#   print(data["Primary Fur Color"][data["Primary Fur Color"] == i].count())
# gray_count = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_count = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_count, cinnamon_count, black_count)
# data_dict = {
#   "color" : ["Gray", "Cinnamon", "Black"], 
#   "count" : [gray_count, cinnamon_count, black_count]
# }

# pandas.DataFrame(data_dict).to_csv("Squirrel_color_count.csv")

screen = turtle.Screen()
screen.title("U.S states games")
screen.addshape('us-states-game-end/blank_states_img.gif')
turtle.shape('us-states-game-end/blank_states_img.gif')


# to get x and y co-ordinates that was clicked
# def pri(x, y):
#   print(x, y)
# screen.onscreenclick(pri)

guessed_states = []
states = pandas.read_csv('us-states-game-end/50_states.csv')
list_states = states.state.tolist()
print(list_states)
while len(guessed_states) < 50:
  answer_state = turtle.textinput(title=f"Guess the state    ({len(guessed_states)}/50)", prompt="What's the another state's name").title()
  print(answer_state)
  if answer_state == "Exit":
    un_guessed = [i for i in states.state if i not in guessed_states]
    # for i in states.state:
    #   if i not in guessed_states:
    #     un_guessed.append(i)
    dict_data = {
      "states": un_guessed
    }
    pandas.DataFrame(dict_data).to_csv("us-states-game-end/states_to_learn.csv")
    break
  if answer_state in list_states and answer_state not in guessed_states:
    guessed_states.append(answer_state)
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.speed("fastest")
    t.goto(int(states["x"][states.state == answer_state]), int(states["y"][states.state == answer_state]))
    t.write(answer_state)
    


screen.mainloop()