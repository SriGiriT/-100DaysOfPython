# first challenge
# year = int(input("year "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year %400 == 0:
#             print("Leap Year")
#         else:
#             print("not a leap year")
#     else: 
#         print("Leap Year")
# else:
#     print("not a leap year")

# final challenge
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz", end=" ")
    elif number % 3 == 0:
        print("Fizz", end=" ")
    elif number % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(number, end=" ")
