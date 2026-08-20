class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"\nAccount number: {self.account_number} \nName: {self.name}, \nBalance: {self.balance}"

    def __repr__(self):
        return f"Account(account_number='{self.account_number}', name='{self.name}', balance={self.balance})"


class Bank:
    def __init__(self):
        self.account = {}

    def create_account(self, account):
        self.account[account.account_number] = account
        return f"Account create success"

    def deposit(self, account_number, money):
        if account_number in self.account and money > 0:
            self.account[account_number].balance = (
                self.account[account_number].balance + money
            )
            self.account[account_number].balance
            return f"Deposit success,\nAccount balance: {self.account[account_number].balance}"
        return False

    def withdraw(self, account_number, money):
        if (
            account_number in self.account
            and money > 0
            and money <= self.account[account_number].balance
        ):
            self.account[account_number].balance = (
                self.account[account_number].balance - money
            )
            return f"Withdraw success,\nAccount balance: {self.account[account_number].balance}"
        return False

    def balance(self, account_number):
        if account_number in self.account:
            return self.account[account_number].balance
        return False

    def transfer(self, from_account_number, to_account_number, money):
        if (
            from_account_number in self.account
            and to_account_number in self.account
            and self.account[from_account_number].balance >= money
            and money > 0
        ):
            self.account[from_account_number].balance = (
                self.account[from_account_number].balance - money
            )
            self.account[to_account_number].balance = (
                self.account[to_account_number].balance + money
            )
            return f"Transfer success {to_account_number} get {money} to account"
        return False


bank = Bank()

jan = Account("11222222223333333333333333", "Jan", 1000)
anna = Account("11222222223333333333333334", "Anna", 500)

bank.create_account(jan)
bank.create_account(anna)
bank.deposit("11222222223333333333333333", 500)
bank.withdraw("11222222223333333333333333", 200)
bank.balance("11222222223333333333333333")
bank.transfer("11222222223333333333333333", "11222222223333333333333334", 300)

print(bank.account)
