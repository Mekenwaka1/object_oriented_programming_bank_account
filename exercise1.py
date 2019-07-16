class BankAccount:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
    
    def __str__(self):
        return "Bank account balance is ${} with an interest_rate of {}%".format(self.balance, self.interest_rate)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def gain_interest(self):
        self.balance += (self.balance * self.interest_rate) 

chequing_account = BankAccount(200, 0.05)
print(chequing_account)
chequing_account.deposit(50)
print(chequing_account)
chequing_account.withdraw(50)
print(chequing_account)
chequing_account.gain_interest()
print(chequing_account)