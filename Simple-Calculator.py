# Simple Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not possible!"
    return a / b

# Main program
print("Welcome to the Simple Calculator!")
print("Available operations:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

while True:
    # User selects operation
    choice = input("\nPlease choose an operation (1-4) or 'q' to quit: ")
    
    # Exit program
    if choice.lower() == 'q':
        print("Calculator is shutting down. Goodbye!")
        break
    
    # Check if input is valid
    if choice not in ['1', '2', '3', '4']:
        print("Invalid input. Please choose 1, 2, 3, 4 or 'q'.")
        continue
    
    # Read numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    # Perform operation
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
