#  property decorator = we use @property decorator on any method 
# in the class to use the method as a property

class Student:
    def __init__(self, math, eng, sci):
        self.math = math
        self.eng = eng
        self.sci = sci
        
    @property
    def percentage(self):
        return str((self.math + self.eng + self.sci) / 3) + "%"
        # @percentage.setter

stu1 = Student(90, 80, 70)
print(stu1.percentage)

stu1.sci = 75
print(stu1.percentage)
