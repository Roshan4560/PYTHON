# recursion : When the functions call itself

# def show(n):  #  to show the number
#     if(n == 0):  # base case
#         return
#     print(n)
#     show(n-1)

# show(6) # 6, 5, 4, 3, 2, 1, 0



def factorial(n):  # to find the factorial of a number
    if(n == 0):  # base case
        return 1
    else:
        return n * factorial(n-1)  # recursive case
    
print("Factorial of 5 is: ", factorial(5))  # 120