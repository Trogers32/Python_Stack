class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if(self.balance < amount):
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.int_rate
            return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print(self.name + " - Balance: $" + str(self.account.balance))
        return self
    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self

Mike = User("Mike", "mikewaz@minc.com")
Donna = User("Donna", "DNA@micro.com")
Neo = User("Anderson", "Neo@matrix.com")

Mike.make_deposit(500).make_deposit(50).make_deposit(5000).make_withdrawal(4000).display_user_balance()

Donna.make_deposit(50).make_deposit(5).make_withdrawal(45).display_user_balance()

Neo.make_deposit(10000).make_withdrawal(500).make_withdrawal(498).make_withdrawal(1).display_user_balance()

Mike.transfer_money(Neo, 550).display_user_balance()
Neo.display_user_balance()