from os import system, name
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
is_on = True
dict = {}
while is_on:
    name = input("Enter your name ? ")
    bit = int(input("Enter the bit: "))
    dict[name] = bit
    if input("is any other bits? ") == "no":
        is_on = False
    if name == "nt":
        system('cls')
    else:
        system("clear")
maxx = 0
person = ""
for i in dict:
    if dict[i] > maxx:
        maxx = dict[i]
        person = i
print(f"Winner is {person} and bit amount {maxx}")
