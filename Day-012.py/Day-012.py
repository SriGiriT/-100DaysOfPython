from random import randint

print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")
answer = randint(1, 101)

def setDifficulty():
  diff = input("Please choose a difficulty level: easy or hard: ")
  if diff == "easy":
    return 10
  elif diff == "hard":
    return 5



count = setDifficulty()
print("you have " + str(count) + " tries")
while count > 0:
  guess = int(input("Guess a number: "))
  if guess == answer:
    print("You guessed the number You win")
    break
  elif guess > answer:
    print("Your guess is too high")
  elif guess < answer:
    print("Your guess is too low")
  count -= 1
  if count == 0:
    print("You lose")
    print("The number was: ", answer)
  else:
    print("you have "+ str(count)+ " guesses left")
    continue
  