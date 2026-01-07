# Simple Calculator using Python
# Codveda Internship - Level 1 Task 1

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    else:
        return a / b


# Main Program
print("===== SIMPLE CALCULATOR =====")

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Display operation menu
print("\nSelect an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1/2/3/4): ")

# Perform selected operation
if choice == '1':
    print("Result:", add(num1, num2))

elif choice == '2':
    print("Result:", subtract(num1, num2))

elif choice == '3':
    print("Result:", multiply(num1, num2))

elif choice == '4':
    print("Result:", divide(num1, num2))

else:
    print("Invalid choice! Please select a valid operation.")
