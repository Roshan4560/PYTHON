# WAP to print the pattern 
#      *
#     * *
#   * * * *
# * * * * * *

# a = int(input("Enter the number :"))

# for i in range(1, a+1):
#     print(" "*(a-i), end="")
#     print("*"*(2*i-1), end="")
#     print("")




# * * *
# *   *
# * * *

a = int(input("Enter the number :"))

for i in range(1, a+1):
    if(i==1 or i==a):
        print("*"*(a), end="")

    else:
        print("*", end="")
        print(" "*(a-2), end="")
        print("*", end="")

    print("")