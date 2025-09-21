#  init function
#  constructor
#  all the  classes have a function called _init_(),which is always executed when the objects is being initiated

#  creating class
class Student:

        # constructor
# self = self parameter is a reference to the current instance of the class, 
# and is used to access variables that belong to the class.
# eg = 
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

s1 =  Student("roshan", 20, 1234)
s2 =  Student("rohit", 21, 1235)
print(s1.name)  # roshan
print(s1.age)  # 20
print(s1.roll_no)  # 1234
print(s2.name)  # rohit
print(s2.age)  # 21
print(s2.roll_no)  # 1235