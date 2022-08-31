from random import randint
from re import L, fullmatch
from tkinter import Y
from turtle import Screen, Turtle, heading, position, width, ycor

# turtle = Turtle()
# screen = Screen()

# Sketch project 
# def move_fd():
#   turtle.fd(10)


# def move_rev():
#   turtle.backward(10)


# def turn_left():
#   turtle.setheading(turtle.heading() + 10)


# def turn_right():
#   turtle.setheading(turtle.heading() - 10)


# def clear():
#   turtle.penup()
#   turtle.home()
#   turtle.clear()
#   turtle.pendown()


# screen.listen()
# screen.onkey(key="w", fun=move_fd)
# screen.onkey(key="s", fun=move_rev)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=clear)

# FINAL PROJECT - TURTLE RACE 

screen = Screen()


screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Make a Bet", prompt="Which turtle will win the race: ")
color = ["red", "green", "yellow", "orange", "blue", "purple"]
turtles = []
position = [-230, -65]

for i in range(len(color)):
  turtles.append(Turtle(shape="turtle"))
  turtles[i].color(color[i])
  turtles[i].penup()
  turtles[i].goto(x=position[0], y=position[1])
  position[1] += 30


is_game_on = False
if user_bet:
  is_game_on = True

while is_game_on:
  for turtle in turtles:
    if turtle.xcor() > 230:
      is_game_on = False
      if user_bet == turtle.pencolor():
        print(f"You win the race the winner is {turtle.pencolor()} ")
      else:
        print(f"You lose the race the winner is {turtle.pencolor()} ")
    turtle.fd(randint(0, 10))

screen.exitonclick()