class BankAccount:
    def __init__(self):
        self.int_rate=0.01
        self.balance=0

    def deposit(self,amount):
        self.balance+=amount
        return self

    def withdraw(self, amount):
        if amount<self.balance:
            self.balance-=amount
        else:
            print("Insufficient funds: %d Charging a $5 fee" % (self.balance))
            self.balance-=5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance>0:
            self.balance+=(self.balance*self.int_rate)
        return self


daniel=BankAccount()
harlow=BankAccount()

daniel.deposit(50).deposit(100).deposit(150).withdraw(75).yield_interest().display_account_info()
harlow.deposit(50).deposit(350).withdraw(5).withdraw(10).withdraw(15).withdraw(20).yield_interest().display_account_info()