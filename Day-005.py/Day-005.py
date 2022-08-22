import random
# Staring
# length = 0
# sum_list = 0
# inputs = input("Enter the data ").split()
# for i in range(0, len(inputs)):
#     inputs[i] = int(inputs[i])
#     sum_list += inputs[i]
#     length += 1
# print(inputs)
# print(length)
# print(sum_list)
# print(sum_list/length)

# Fizz Buzz 
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz", end=" ")
#     elif i % 3 == 0:
#         print("Fizz", end=" ")
#     elif i % 5 == 0:
#         print("Buzz", end=" ")
#     else:
#         print(i, end=" ")
# Final Challenge
# My approach
print("Welcome to the pyPassword Generator!")
length = int(input("Enter the total length "))
len_symbols = int(input("Enter the length of symbols "))
len_numbers = int(input("Enter the length of numbers "))
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbol = "\"\'\\/!@#$%^&*()_+-={}[]|:;<>,.`~"
list_answer = []
for i in range(length-len_numbers-len_symbols):
    list_answer.append(alpha[random.randint(0, len(alpha)-1)])
for i in range(len_symbols):
    list_answer.append(symbol[random.randint(0, len(symbol))])
for i in range(len_numbers):
    list_answer.append(digits[random.randint(0, 9)])
random.shuffle(list_answer)
for i in list_answer:
    print(i, end="")
