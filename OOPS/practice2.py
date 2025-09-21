# class & instance attributes

class Student:
    # class variable
    # this is commaon for all the objects of the class
    school_name = "ABC School"
    
    def __init__(self, name, age, roll_no):
        # instance variables
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def welcome(self):
        print("Welcome students")
        print(f"Welcome to {self.school_name}")
        print("Welcome students", self.name)


    def get_age(self):
        return self.age
        

s1 =  Student("roshan", 20, 1234)
s2 =  Student("rohit", 21, 1235)

print(s1.name)  # roshan
print(s1.age)  # 20
print(s1.roll_no)  # 1234
print(s1.school_name)  # ABC School

print(s1.welcome())  # Welcome to ABC School
print(s2.name)  # rohit
print(s2.age)  # 21
print(s2.roll_no)  # 1235
print(s2.school_name)  # ABC School

#  print the age 
print(s1.get_age())  # 20