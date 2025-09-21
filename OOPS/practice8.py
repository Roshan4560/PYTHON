#  private(like)  attributes and methods 

# conceptual Implementations in python 
# private attributes and methods are meant to be used 
# only within the class are not accessible from outside the class 

class Account:
    def __init_(self, acc_no, acc_pass):  # if we write __init_ means class is private
        self.acc_no = acc_no     # other wise class is public
        self.acc_pass = acc_pass

acc1 = Account("12345", "abcde")

print(acc1.acc_no)
print(acc1.acc_pass)