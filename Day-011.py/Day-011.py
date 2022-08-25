import random
from os import name, system

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)


def calculate_score(cards):
  if len(cards) == 2 and sum(cards) == 21:
    return 0
  while 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def compare(user_score, computer_score):
  if user_score == computer_score:
    return 'Draw'
  elif user_score == 0:
    return "You won and got a black jack"
  elif computer_score == 0:
    return "You lost computer got a black jack"
  elif user_score > 21:
    return "You lost you went over"
  elif computer_score > 21:
    return "you win"
  elif user_score > computer_score:
    return "You won"
  else:
    return "You lost"


def card_game():
  user_cards = []
  computer_cards = []
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  print(logo)
  is_game_over = False
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards} with score: {user_score}")
    print(f"computer's first card is: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
      is_game_over = True
    else:
      if input("if you want another card enter 'y'")=="y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
  while computer_score <17 and computer_score != 0:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  print(f"Your cards: {user_cards} with score: {user_score}")
  print(f"computer's cards: {computer_cards} with score: {computer_score}")
  print(compare(user_score, computer_score))
  if input("You want to play again y/n ") == "y":
    if(name == "nt"):
      system("cls")
    else:
      system("clear")
    card_game()
  else:
    print("Bye")


card_game()