# practice question
#  Create student class that takes name and marks of 3 subjects as argument in constructor.
#  Then create a method to print the aversge

class Student:

    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        
    def average(self):
        avg = (self.marks1 + self.marks2 + self.marks3) / 3
        return avg

s1 = Student("roshan", 85, 90, 95)
s2 = Student("rohit", 80, 85, 90)
s3 = Student("ravi", 75, 80, 85)
s3.name = "Ram" # changing name of s3 object

print(s1.name,s1.marks1,s1.marks2,s1.marks3)  # roshan 85 90 95
print("Average is :",s1.average())  # 90.0

print(s2.name,s2.marks1,s2.marks2,s2.marks3)  # rohit 80 85 90
print("Average is :",s2.average())  # 85.0

print(s3.name,s3.marks1,s3.marks2,s3.marks3)  # ravi 75 80 85
print("average is :",s3.average())  # 80.0