from os import system, name
logo = '''
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
'''


def add(x, y):
  return x + y


def sub(x, y):
  return x - y


def multiply(x, y):
  return x * y


def divide(x, y):
  return x / y


dictionary_calculator = {
  "+": add, 
  "-": sub,
  "*": multiply,
  "/": divide
}


is_on = True
def calculator():
  print(logo)
  is_on = True
  num1 = float(input("Enter first number: "))
  for i in dictionary_calculator:
    print(i)
  while is_on:
    operator = input("Enter operator: ")
    num2 = float(input("Enter second number: "))
    answer = dictionary_calculator[operator](num1, num2)
    print(f"{num1} {operator} {num2} = {answer}")
    if input("Do you want to continue? (y/n) ") == "y":
      num1 = answer
    else:
      is_on = False
      if(name == 'nt'):
        system('cls')
      else:
        system('clear')
      calculator()


calculator()
