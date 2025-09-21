# WAP to print and show the ternary operator 


# <var> = (false_val, true_val) [<condition>]
age = int(input("Enter the age :"))
vote = ("NO", "YES")  [age>=18]
print(vote)