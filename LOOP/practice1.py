# #  print the multiplication table of a number n

# print("Enter the number for multiplication table")
# n = int(input("Enter the number: "))
# x = 1
# while x <= 10:
#     print(n, "*", x, "=", n * x)
#     x += 1



# print the elements of the following list using a loop
# list1 = [1,4,9,16,25,36,49,64,81,100]

# i = []
# n = 1
# while n <= 10:
#     i.append(n * n)
#     n += 1
# print(i)



#  print the list by the use of loop
# list1 = [1,4,9,16,25,36,49,64,81,100]

# idx  = 0
# while idx < len(list1):
#     print(list1[idx])
#     idx += 1




# Search for a number x in this tuple usinf loop
tuple1 = (1,4,9,16,25,36,49,64,81,100)
print("The number to search")
x = int(input("Enter the number: "))
idx = 0
while idx < len(tuple1):
    if tuple1[idx] == x:
        print("The number is found at index", idx+1)
        break
    idx += 1
else:
    print("The number is not found in the tuple")