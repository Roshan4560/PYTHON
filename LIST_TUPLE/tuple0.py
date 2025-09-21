#  tuple
#  tuple is immutable means we can't change the value of tuple after it is created.
#  tuple is created by using () brackets.
#  tuple is used to store multiple items in a single variable. it is similar to list

tup = (1, 2, 3, 4, 5)
print(tup)
print(type(tup))
print(len(tup)) # length of tuple
print(tup[0]) # first element of tuple
tup1 = (1, ) # tuple with single element. if we don't use comma, it will be treated as int
print(type(tup1)) # tuple with single element
print(tup1)