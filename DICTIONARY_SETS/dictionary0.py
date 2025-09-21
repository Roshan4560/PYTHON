#  This is a dictionary in Python
#  A dictionary is a collection of key:value pairs.
#  Each key is unique and maps to a value.
#  They are mutable (changeable), unordered, and indexed.

info = {
    "name": "roshan",
    "age": 20,
    "course": "python",
    "is_student": True,
}

print(info)
print(type(info))
print(info["name"])  # Accessing value using key

# we can reassign the value of a key
info["name"] = "roshan kumar"
print(info["name"])  # Accessing value using key

# we can create a null dictionary
null_dict = {}