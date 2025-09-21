# range = range functions returns a sequence of numbers, 
# starting from 0 by default, and increments by 1 (by default), 
# and stops before a specified number.


range(10) # 0,1,2,3,4,5,6,7,8,9
print(list(range(10))) 

# for i in range(10):  # range(stop)
#     print(i)

# for i in range(1, 10): # range(start, stop)
#     print(i)

for i in range(1, 10, 3):  # range(start, stop, step)
    print(i)