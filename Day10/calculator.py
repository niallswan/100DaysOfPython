import art

# Print ASCII art
print(art.logo)

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Dictionary
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

# Prompt user for first number
num1 = float(input("What's the first number?: "))

# Print the operation symbols
for symbol in operations:
    print(symbol)
# Prompt user for operation choice
operation_symbol = input("Pick an operation from the lines above: ")

# Prompt user for second number
num2 = float(input("What's the second number?: "))

# Find the operation function using the symbol and pass it num1 and num2 to get the answer
first_answer = operations[operation_symbol](num1, num2)

# Print answer
print(f"{num1} {operation_symbol} {num2} = {first_answer}")

# Ask if user wants to keep calculating
keepGoing = input(f"Type 'y' to continue calculating with {first_answer} or type 'n' to exit.: ").lower()

while keepGoing == 'y':
    operation_symbol = input("Pick another operation: ")

    num3 = float(input("What's another number?: "))

    second_answer = operations[operation_symbol](first_answer, num3)

    print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

    keepGoing = input(f"Type 'y' to continue calculating with {first_answer} or type 'n' to exit.: ")

# Exit
print("Goodbye!")





