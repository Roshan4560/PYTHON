# OOPS
# To map with real world scenarious,we started uing objects in code
# This is called OOPS (Object Oriented Programming)


#  CLASS & OBJECTS IN PYTHON
# class is a blueprint for creating objects

# creating class
#   class Student:
#     # class variables
#     name = "roshan"
#     age = 20
#     roll_no = 1234


# creating object of class(instance of class)
#   s1 = Student()
# print(s1)  # <__main__.Student object at 0x7f8c4c2b3d90>




class Student:
    name = "roshan"


s1 = Student()
print(s1)
print(s1.name) # roshan



class car:
    color = "red"
    model = "audi"
    year = 2023
    price = 1000000

car1 = car()
car2 = car()

print(car1.color)  # red
print(car2.color)  # red
print(car1.model)  # audi