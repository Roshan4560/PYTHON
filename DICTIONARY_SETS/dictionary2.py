# DICTIONARY METHODS

dict = {
    "name": "roshan",
    "age": 20,
    "course": "python",
    "is_student": True,
    "marks": {
        "math": 90,
        "science": 85,
        "english": 88,
    },
    "hobbies": ["reading", "coding", "gaming"],
}

# 1. dict.keys() - Returns a view object that displays a list of all the keys in the dictionary.
print("Keys:", dict.keys())


# 2. dict.values() - Returns a view object that displays a list of all the values in the dictionary.
print("Values:", dict.values())


# 3. dict.items() - Returns a view object that displays a list of a dictionary's key-value tuple pairs.
print("Items:", dict.items())

# 4. dict.get(key) - Returns the value for the specified key if the key is in the dictionary.
# If not, it returns None (or a specified default value).
print("Get 'name':", dict.get("name"))

# 5. dict.update(other_dict) - Updates the dictionary with the key-value pairs from another dictionary.
# If the key already exists, its value is updated; if not, a new key-value pair is added.
dict.update({"city": "Kathmandu"})
print("Updated Dictionary:", dict)