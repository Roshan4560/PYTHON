# Write a recursive function to calculate the sum of first n natural numbers 

print("Enter the number :")
n = int(input())

def sum_natural(n):  # to find the sum of first n natural numbers
    if(n == 0):  # base case
        return 0
    else:
        return n + sum_natural(n-1)  # recursive case
    
print("Sum of first", n, "natural numbers is: ", sum_natural(n))  # 15