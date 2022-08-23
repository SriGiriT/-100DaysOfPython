# challenge of Day-002
# age = int(input("What is your current age : "))
# print(f"You have {(90-age)*365} days, {(90-age)*52} weeks and {(90-age)*12} months left.")

# Final challenge of Day-002 
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
percentage = int(input("What percentage tip would like to give? 10, 12, or 15? "))
total_persons = int(input("How many people to split the bill? "))
print(f"Each person should pay: ${round((((bill * (percentage*0.01)) + bill) / total_persons), 2)}")
 