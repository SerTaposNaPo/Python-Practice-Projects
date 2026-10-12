from datetime import datetime

def main():
    bank = Bank()
    while True:
        print("=== Island Bank ===")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        answer = int(input("Answer : "))
        if answer == 1:
            name = input("Name : ")
            starting_balance = int(input("Balance : "))
            bank.create_account(name, starting_balance)
        elif answer == 2:
            name = input("Bank Name : ")
            amount = int(input("Balance : "))
            bank.deposit(name, amount)
        elif answer == 3:
            name = input("Bank Name : ")
            amount = int(input("Balance : "))
            bank.withdraw(name, amount)
        elif answer == 4:
            name = input("Bank Name : ")
            account = bank.accounts[name]
            print(account.get_balance())

        elif answer == 5:
            break

class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount
        self.datetime = datetime.now()


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid Deposit")
        else:
            self.balance += amount
            self.transactions.append(Transaction("Deposit", amount))

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid Withdraw")
        elif amount > self.balance:
            raise InsufficientFundsError("Insufficient Balance")
        else:
            self.balance -= amount
            self.transactions.append(Transaction("Withdraw", amount))

    def get_balance(self):
        return self.balance

    def print_statement(self):
        print()
        print("=== Bank Statement ===")
        for transaction in self.transactions:
            print(f"Transaction Type : {transaction.transaction_type}")
            print(f"Amount : {transaction.amount}")
            print(f"Date and Time : {transaction.datetime}")


class Bank:
    def __init__(self,):
        self.accounts = {}

    def create_account(self, name, starting_balance):
        account = Account(name, starting_balance)
        self.accounts[name] = account

    def deposit(self, name, amount):
        account = self.accounts[name]
        account.deposit(amount)

    def withdraw(self, name, amount):
        account = self.accounts[name]
        try:
            account.withdraw(amount)
        except InsufficientFundsError as e:
            print(e)

class InsufficientFundsError(Exception):
    pass

if __name__ == "__main__":
    main()