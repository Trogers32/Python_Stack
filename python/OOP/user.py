class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.name + " " + str(self.account_balance))
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

Mike = User("Mike", "mikewaz@minc.com")
Donna = User("Donna", "DNA@micro.com")
Neo = User("Anderson", "Neo@matrix.com")

Mike.make_deposit(500).make_deposit(50).make_deposit(5000).make_withdrawal(4000).display_user_balance()

Donna.make_deposit(50).make_deposit(5).make_withdrawal(45).display_user_balance()

Neo.make_deposit(10000).make_withdrawal(500).make_withdrawal(498).make_withdrawal(1).display_user_balance()

Mike.transfer_money(Neo, 550).display_user_balance()
Neo.display_user_balance()