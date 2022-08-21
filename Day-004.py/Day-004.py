import random

# Day-004 challenge
# row1 = ["0", "0", "0"]
# row2 = ["0", "0", "0"]
# row3 = ["0", "0", "0"]
# mapp = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = int(input("Where to place? "))
# row = position % 10 - 1
# col = position // 10 - 1
# mapp[row][col] = "X"
# print(f"{row1}\n{row2}\n{row3}")

# Day-004 Final Challenge
lis = [
'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''',
'''
    _______
---'   ____)____ 
          ______)
       __________)
      (____)
---.__(___)
'''
    ]
human_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors. "))
print(lis[human_choice])
computer_choice = random.randint(0, 2)
print(f"computer choose {computer_choice}")
print(lis[computer_choice])
if(human_choice == 0 and  computer_choice == 2):
    print("You win!")
elif(human_choice == 2 and  computer_choice == 0):
    print("You lose!")
elif(human_choice > computer_choice):
    print("You win!")
elif(human_choice < computer_choice):
    print("You lose!")
elif (human_choice == computer_choice):
    print("You Draw")
else:
    print("Invalid input")
