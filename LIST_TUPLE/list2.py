# LIST METHODS 

list = [2,1,3,6]

# 1. list.append() - Adds an element to the end of the list   // [2,1,3,6,5]
list.append(5)
print(list)

# 2. list.extend() - Adds multiple elements to the end of the list   // [2,1,3,6,5,4,3]
list.extend([4,3])
print(list)

# 3. list.insert() - Inserts an element at a specific index   // [2,1,3,6,5,4,3,0]
list.insert(7,0)
print(list)

# 4. list.remove() - Removes the first occurrence of a specific element   // [1,3,6,5,4,3,0]
list.remove(2)
print(list)

# 5. list.pop() - Removes and returns the last element of the list   // [1,3,6,5,4,3]
list.pop()
print(list)

# 6. list.clear() - Removes all elements from the list   // []
list.clear()
print(list)

# 7. list.sort() - Sorts the elements of the list in ascending order   // [1,2,3,4,5,6]
list = [2,1,3,6,5,4]
asa = ["a", "c", "b", "q", "e"]
list.sort()
asa.sort()
print(list)
print(asa)

# 8. list.sort(reverse=True) - Reverses the order of the elements in the list   // [6,5,4,3,2,1]
list.sort(reverse=True)
print(list)

# 9. list.index(idx,element) - insert element at index idx   
list.insert(2, 7)
print(list)