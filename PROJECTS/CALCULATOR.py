# WAP to create a simple calculator that can perform 
# addition, subtraction, multiplication, and division.


def add(x, y):  # add the number
    return x + y

def subtract(x, y):  # subtract the number
    return x - y

def multiply(x, y):  # multiply the number
    return x * y

def divide(x, y):  # divide the number
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

print("Simple Calculator")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':    # uses if-else statements to check the choice
    print(f"Result: {add(num1, num2)}")
elif choice == '2':
    print(f"Result: {subtract(num1, num2)}")
elif choice == '3':
    print(f"Result: {multiply(num1, num2)}")
elif choice == '4':
    print(f"Result: {divide(num1, num2)}")
else:
    print("Invalid input")