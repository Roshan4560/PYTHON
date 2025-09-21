# pass = pass is a null statement in Python.
# It is a placeholder that is syntactically required but does not perform any action.

# for i in range(5):
#     pass  # This loop does nothing, but it is syntactically correct.

# print("someuseful code here")



# WAP to find the sum of first n natural numbers 

# i = 1
# sum = 0
# while i <= 10:
#     sum += i
#     i += 1

# print("The sum of first 10 natural numbers is:", sum)





# WAP to find the factorial of a number

print("Enter a number to find its factorial:")
x = int(input())
for i in range(1, x+1):
    if i == 1:
        fact = 1
    else:
        fact = fact * i

print("The factorial of", x, "is:", fact)