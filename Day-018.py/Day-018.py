from random import choice, randint
from turtle import Turtle, Screen, colormode, hideturtle
# import colorgram

turtle = Turtle()
# turtle.shape("turtle")
screen = Screen()



# code to draw dashed lines 
# n = 15
# while n>0:
#   turtle.fd(10)
#   turtle.penup()
#   turtle.fd(10)
#   turtle.pendown()
#   n -= 1


# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
# to turn according to the side we need to divide sides with 360 
# eg. for square 360/4 = 90
# colors = ["red", "orange", "brown", "yellow", "green", "blue", "purple", "black"]
# n = 3
# while n <=10:
#   degree = 360 / n
#   temp = n
#   turtle.color(choice(colors))
#   while temp > 0:
#     turtle.right(degree)
#     turtle.fd(100)
#     temp -= 1
#   n += 1

# Random walk


def random_color():
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  return (r, g, b)


colormode(255)
# angles = [0, 90, 180, 270, 360]
# colors = ["red", "orange", "brown", "yellow", "green", "blue", "purple", "black"]
# turtle.pensize(15)
# turtle.speed(10)
# while True:
#   turtle.right(choice(angles))
#   turtle.color(random_color())
#   turtle.fd(30)


# draw Spirograph
# turtle.speed(0)
# def draw_spirograph(size):
#   for i in range(360 // size):
#     turtle.color(random_color())
#     turtle.setheading(turtle.heading()+size)
#     turtle.circle(100)
# draw_spirograph(1)

# final challenge
# colors = colorgram.extract('color.jpg', 30)
# rgb_colors = []
# for color in colors:
#   rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
# print(rgb_colors)
color = [(253, 251, 247), (254, 249, 252), (234, 251, 243), (197, 13, 32), (249, 237, 21), (39, 77, 188), (238, 227, 5), (39, 216, 68), (228, 160, 47), (243, 247, 253), (28, 40, 155), (214, 75, 14), (16, 153, 17), (199, 15, 11), (242, 34, 164), (226, 19, 120), (74, 9, 31), (60, 15, 8), (223, 141, 208), (11, 97, 62), (220, 160, 10), (18, 18, 43), (52, 211, 230), (11, 228, 239), (80, 73, 214), (238, 156, 217), (73, 212, 168), (81, 234, 202), (61, 233, 241), (5, 67, 42)]
# My approach 
# row = 0
# col = 0
# x = -250
# y = -250
# while row < 10:
#   turtle.penup()
#   turtle.goto(x, y)
#   turtle.pendown()
#   while col < 10:
#     turtle.dot(20, choice(color))
#     turtle.penup()
#     turtle.fd(50)
#     turtle.pendown()
#     col += 1
#   y += 50
#   row += 1
#   col = 0

# Course approach
turtle.penup()
turtle.hideturtle()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
number_of_dots = 100

for dot in range(1, number_of_dots+1):
  turtle.dot(20, choice(color))
  turtle.fd(50)
  if dot % 10 == 0:
    turtle.setheading(90)
    turtle.fd(50)
    turtle.setheading(180)
    turtle.fd(500)
    turtle.setheading(0)
screen.exitonclick()