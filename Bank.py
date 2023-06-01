class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} has been deposited. New balance is ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds. Balance is ${self.balance}")
        else:
            self.balance -= amount
            print(f"${amount} has been withdrawn. New balance is ${self.balance}")
    
    def check_balance(self):
        print(f"Account balance is ${self.balance}")

my_account = BankAccount("John Doe", "123456789")

my_account.deposit(500)
my_account.withdraw(200)
my_account.check_balance()

