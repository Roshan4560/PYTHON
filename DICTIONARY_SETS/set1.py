# SETS METHODS 

se = {1, 2, 3, 4, 5}

se.add(6) # add an element to the set
print(se) # {1, 2, 3, 4, 5, 6}

se.update([7, 8, 9]) # add multiple elements to the set
print(se) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

se.remove(9) # remove an element from the set
print(se) # {1, 2, 3, 4, 5, 6, 7, 8}

se.discard(8) # remove an element from the set, if it exists
print(se) # {1, 2, 3, 4, 5, 6, 7}

se.pop() # remove and return an arbitrary element from the set
print(se) # {2, 3, 4, 5, 6, 7} (the element removed is arbitrary)

se.clear() # remove all elements from the set
print(se) # set() (the set is now empty)

# in a set we can add the string ,integer, float, tuple, frozenset, and other set
# but we can't add the list, dictionary, and set itself
# because they are mutable

se = {1, 2, 3, 4, 5}

se.add("hello") # add a string to the set
print(se) # {1, 2, 3, 4, 5, 'hello'}

se.add(3.14) # add a float to the set
print(se) # {1, 2, 3, 4, 5, 'hello', 3.14}

se.add((1, 2)) # add a tuple to the set
print(se) # {1, 2, 3, 4, 5, 'hello', 3.14, (1, 2)}

se.add(frozenset({1, 2})) # add a frozenset to the set
print(se) # {1, 2, 3, 4, 5, 'hello', 3.14, (1, 2), frozenset({1, 2})}

se.add([1,2]) # add a list to the set (will raise an error)
print(se) # TypeError: unhashable type: 'list'