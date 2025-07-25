# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

# Get user input for the operation
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    try:
        choice = input("Enter choice(1/2/3/4): ")
        if choice not in ('1', '2', '3', '4'):
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        break  # Exit the loop if input is valid
    except ValueError:
        print("Invalid input. Please enter a number.")

# Perform the calculation based on the user's choice
if choice == '1':
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")
elif choice == '2':
    result = subtract(num1, num2)
    print(f"{num1} - {num2} = {result}")
elif choice == '3':
    result = multiply(num1, num2)
    print(f"{num1} * {num2} = {result}")
elif choice == '4':
    result = divide(num1, num2)
    print(f"{num1} / {num2} = {result}")