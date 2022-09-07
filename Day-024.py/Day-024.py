from turtle import Screen, Turtle
from time import sleep 
from snake import Snake
from food import Food
from scoreboard import Score


def game():
  screen = Screen()
  screen.setup(width=600, height=600)
  screen.bgcolor("black")
  screen.title("MY Snake Game")

  screen.tracer(0)
  snake = Snake()
  food = Food()
  score = Score()
  screen.listen()
  screen.onkey(snake.up, "Up")
  screen.onkey(snake.up, "w")
  screen.onkey(snake.down , "Down")
  screen.onkey(snake.down, "s")
  screen.onkey(snake.left , "Left")
  screen.onkey(snake.left, "a")
  screen.onkey(snake.right , "Right")
  screen.onkey(snake.right, "d")
  is_game_on = True
  while is_game_on:
    screen.update()
    sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
      snake.extend()
      score.addScore()
      food.refresh()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
      score.game_over()
      is_game_on = False
      sleep(2)

    for segment in snake.snake[1:]:
      if snake.head.distance(segment) < 10:
        score.game_over()
        is_game_on = False
        sleep(2)

    if is_game_on == False:
      screen.clear()
      screen.bgcolor("black")
      to_continue = screen.textinput("Again?", "Do you want to play again? ")
      if to_continue == "yes":
        score.reset_score()
        game()
      else:
        pass

  screen.exitonclick()
game()