# functions : It is a block of statements that performs a specific task.

# def fun_name(param1, param2):
#  some work : return value

# def sum (a, b):
#     return a + b

# print(sum(10, 20)) # 30
# print(sum(12, 25)) # 37
# print(sum(15, 22)) # 37
# print(sum(108, 202)) # 310

#  fun_name(param1, param2) : function call



# Averge of 3 numbers

def average(a, b, c):
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))

    avg = (a + b + c) / 3
    return avg

print("Average of 3 numbers is: ", average(0, 0, 0)) # 0, 0, 0 are dummy values