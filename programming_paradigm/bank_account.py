class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 500

    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance
    def withdraw(self, amount):
        self.account_balance -= amount
        return True if self.account_balance >= amount else False
    def display_balance(self, amount):
        print(f"Current Balance:{self.account_balance}")
