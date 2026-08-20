class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"\nAccount number: {self.account_number} \nName: {self.name}, \nBalance: {self.balance}"

    def __repr__(self):
        return f"Account(account_number='{self.account_number}', name='{self.name}', balance={self.balance})"

    def is_positive_amount(self, amount):
        return amount > 0

    def deposit(self, amount):
        if self.is_positive_amount(amount):
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if self.balance >= amount and self.is_positive_amount(amount):
            self.balance -= amount
            return True
        return False


class Bank:
    def __init__(self):
        self.account = {}

    def create_account(self, account):
        self.account[account.account_number] = account
        return f"Account create success"

    def deposit(self, account_number, amount):
        if account_number in self.account:
            self.account[account_number].deposit(amount)
        return False

    def withdraw(self, account_number, amount):
        if account_number in self.account:
            self.account[account_number].withdraw(amount)
        return False

    def transfer(self, from_account_number, to_account_number, amount):
        if from_account_number in self.account and to_account_number in self.account:
            from_acc = self.account[from_account_number]
            to_acc = self.account[to_account_number]
            if from_acc.withdraw(amount):
                to_acc.deposit(amount)
                return f"Transfer success {to_account_number} get {amount} to account"
        return False


bank = Bank()

jan = Account("11222222223333333333333333", "Jan", 1000)
anna = Account("11222222223333333333333334", "Anna", 500)

bank.create_account(jan)
bank.create_account(anna)
bank.deposit("11222222223333333333333333", 500)
bank.withdraw("11222222223333333333333333", 200)
bank.transfer("11222222223333333333333333", "11222222223333333333333334", 300)


print(bank.account)
