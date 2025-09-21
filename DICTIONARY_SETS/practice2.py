# # WAP to enter marks of 3 students from the user and store them in a dictionary.
# # Start with empty dictionary and add one by one.
# # Use subject name as key and marks as value.


# # this is a without entering the data from the user
# report ={}
# print(report)
# Roshan = {
#     "Hindi": 90,
#     "English": 95,
#     "Maths": 99,
#     "Science": 98,
#     "Social": 97,
# }
# report.update(Roshan)
# print(report)

# Shyam = {
#     "Hindi": 85,
#     "English": 90,
#     "Maths": 95,
#     "Science": 96,
#     "Social": 94,
# }
# report.update(Shyam)
# print(report)

# Mohan = {
#     "Hindi": 80,
#     "English": 85,
#     "Maths": 90,
#     "Science": 92,
#     "Social": 91,
# }
# report.update(Mohan)
# print(report)


# this is a with entering the data from the user

report = {}
print(report)

x = int(input("Enter the physics marks: "))
report.update({"Physics": x})

x = int(input("Enter the chemistry marks: "))
report.update({"Chemistry": x})

x = int(input("Enter the maths marks: "))
report.update({"Maths": x})

print(report)