#  Create account class with 2 attributes - balance and account number
#  Create a method for debit and credit and display balance

class Account:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Debited {amount}. New balance is {self.balance}")

    def credit(self, amount):
        self.balance += amount
        print(f"Credited {amount}. New balance is {self.balance}")

    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")

# Create an instance of the Account class
account = Account(1000, "123456789")
# Display initial balance
account.display_balance()
# Debit and credit operations
account.debit(200)
account.credit(500)
# Display final balance
account.display_balance()
# Output:
# Account Number: 123456789, Balance: 1000
# Debited 200. New balance is 800
# Credited 500. New balance is 1300
# Account Number: 123456789, Balance: 1300