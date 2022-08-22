import random
import os

hang = ["""
   +---+
   |   |
       |
       |
       |
       | 
=========""", """
  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]
words = ["random", "words", "for", "hangman", "game", "was", "kind", "of", "cool"]
word = random.choice(words)
c = 0
ans = ["_" for i in range(len(word))]
for j in ans:
    print(j, end="")
print()
print("Guess the word")
while "_" in ans:
    inp = input()
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
    if(inp in word and inp not in ans):
        print(hang[c])
        for i in range(len(word)):
            if inp == word[i]:
                ans[i] = word[i]
        for j in ans:
            print(j, end="")
        print()
    elif(inp in ans):
        print("Already Guessed !!!")
        print(hang[c])
    else:
        if(c < 6 ):
            print(hang[c])
            c+=1
            for j in ans:
                print(j, end="")
            print()
        else:
            print(hang[c])
            print("you lose ")
            break
if c < 6:
    print("You win!!!")
