#  del keyword  =  used to delete object properties or object itself

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("John", 20)
print(s1)     # in this code s1 is giving the output of the object
del s1
print(s1)     # in this code s1 is giving the error because we have deleted the object