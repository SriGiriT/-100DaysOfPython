MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    for items in order_ingredients:
        if order_ingredients[items] > resources[items]:
            print(f"Sorry there is no resource to make your order")
            return False
    return True


def make_transaction():
    print("please enter coins")
    total = int(input("How many quarters? "))*.25
    total += int(input("How many dimes? "))*.1
    total += int(input("How many nickles? "))*.05
    total += int(input("How many pennies? "))*.01
    return total


def is_transaction_successful(money, drink_cost):
    if money >= drink_cost:
        print(f"Have your change {round(money-drink_cost, 2)}")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"You don't have enough money to make it")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} Enjoy!!!")


isOn = True
while isOn:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        isOn = False
    elif choice == "report":
        print(f"water {resources['water']}ml")
        print(f"milk {resources['milk']}ml")
        print(f"coffee {resources['coffee']}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            pay = make_transaction()
            if is_transaction_successful(pay, drink['cost']):
                make_coffee(choice, drink['ingredients'])


#### MY approach ####

# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
#
# def is_ingredients(drink):
#     for items in drink['ingredients']:
#         if resources[items] < drink['ingredients'][items]:
#             print("not enough resources ")
#             return False
#     return True
#
#
# def process_coin():
#     print("please enter coins")
#     total = int(input("How many quarters? ")) * .25
#     total += int(input("How many dimes? ")) * .1
#     total += int(input("How many nickles? ")) * .05
#     total += int(input("How many pennies? ")) * .01
#     return total
#
#
# def make_payment(pay, drink, choice):
#     if pay < drink['cost']:
#         print("your can't able to make it ")
#         return False
#     else:
#         print(f"take your change {round(pay-drink['cost'], 2)} ")
#         global profit
#         profit += drink['cost']
#         for items in drink['ingredients']:
#             resources[items] -= drink['ingredients'][items]
#         print(f"Here is your coffee {choice} Enjoy!!")
#         return True
#
#
# isOn = True
# while isOn:
#     choice = input("What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         print("power off")
#         isOn = False
#     elif choice == "report":
#         print(f"water {resources['water']}ml")
#         print(f"milk {resources['milk']}ml")
#         print(f"coffee {resources['coffee']}ml")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_ingredients(drink):
#             pay = process_coin()
#             if make_payment(pay, drink, choice):
#                 pass
