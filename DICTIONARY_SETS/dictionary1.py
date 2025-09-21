#  nested loop dictionary
#  A dictionary can contain other dictionaries as values.

dict = {
    "name" : "Roshan",
    "course" : "python",
    "marks" : {
        "math": 90,
        "science": 85,
        "english": 88,
    },
    "age": 20,
}

print(dict["marks"]["math"])  # Accessing nested dictionary value
print(dict["marks"])  # Accessing nested dictionary
print(dict)  # Accessing dictionary