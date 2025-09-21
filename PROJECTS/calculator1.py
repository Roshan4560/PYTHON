#  WAP to make a simple calculator using class and object

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

# User input
calc = Calculator()
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Choose operation (+ for the 'a' and 'A', - for the 's' and 'S', * for the 'm' and 'M', / for the 'd' and 'D'): ")

if operation == 'a' or operation == 'A':
    print("Result:", calc.add(a, b))
elif operation == 's' or operation == 'S':
    print("Result:", calc.subtract(a, b))
elif operation == 'm' or operation == 'M':
    print("Result:", calc.multiply(a, b))
elif operation == 'd' or operation == 'D':
    print("Result:", calc.divide(a, b))
else:
    print("Invalid operation")