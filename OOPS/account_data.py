#  create a an account class with methods to deposit, withdraw and check balance

class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")
    def check_balance(self):
        print(f"Current balance is {self.balance}.")

# create an account object
account1 = Account("123456789", "John Doe", 1000)
# deposit money
account1.deposit(500)
# withdraw money
account1.withdraw(200)
# check balance
account1.check_balance()


# create another account object
account2 = Account("987654321", "Jane Doe", 2000)
# deposit money
account2.deposit(1000)
# withdraw money
account2.withdraw(500)
# check balance
account2.check_balance()