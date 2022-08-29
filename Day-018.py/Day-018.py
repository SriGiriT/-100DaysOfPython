from random import choice, randint
from turtle import Turtle, Screen, colormode

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


# colormode(255)
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
# screen.exitonclick()