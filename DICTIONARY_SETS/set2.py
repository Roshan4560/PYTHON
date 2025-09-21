#  SETS METHODS (Basic but most important methods)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1.union(set2)) # returns a new set with all elements from both sets
# set1.union(set2) # returns a new set with all elements from both sets
# return {1, 2, 3, 4, 5, 6, 7, 8}

print(set2.intersection(set1)) # returns a new set with elements common to both sets
# set1.intersection(set2) # returns a new set with elements common to both sets
# return {4, 5}