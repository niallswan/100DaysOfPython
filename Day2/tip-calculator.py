#Greeting
print("Welcome to the tip calculator.")

#Prompt for total bill
totalBill = float(input("What was the total bill? $"))

#Prompt for the percentage of tip
tipPercentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

#Prompt for the amount of people to split the bill between
billSplit = int(input("How many people to split the bill? "))

#Calculate result to 2 decimal places
result = "{:.2f}".format(round((totalBill * (1 + tipPercentage / 100)) /  billSplit, 2))
print(f"Each person should pay: ${result}")