# SETS
# Set is a collection of unordered and unindexed items. It is mutable and does not allow duplicates.
# Set is defined by curly brackets {} or the set() function.
# Set is iterable, but it does not support indexing, slicing, or other sequence-like behavior.
# Set can contain any immutable data type, such as strings, numbers, or tuples.
# Set can be used to perform mathematical operations like union, intersection, difference, etc.
# Set is mutable, meaning you can add or remove elements from it after creation.
# In set you cannot perform list operations and dictionary operations.


# Example of set
nums = {1, 2, 3, 4, 5}
print(nums)  # Output: {1, 2, 3, 4, 5}  # Duplicates are ignored in set
print(type(nums))  # Output: <class 'set'>
print(len(nums))  # Output: 5  # Length of set

aa = {1, 2, 3, "hello", "world", "world", 4, 5}
print(aa)  # Output: {1, 2, 3, 'hello', 'world', 4, 5}  # Duplicates are ignored in set
# set is unordered, so the order of elements may vary


# empty set
empty_set = set()
print(empty_set)  # Output: set()  # Empty set
print(type(empty_set))  # Output: <class 'set'>  # Type of empty set