class User:
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.account_balance=0
    
    def make_deposit(self, amount):
        self.account_balance+=amount
        return self
    
    def make_withdrawl(self, amount):
        self.account_balance-=amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name} Balance: ${self.account_balance}")
        return self

    def transfer_money(self,exceptor,amount):
        if amount<self.account_balance:
            b_string="Before transfer - User: %s's Balance: %d, Exceptor's User: %s's Balance: %d" \
                %(self.name, self.account_balance, exceptor.name, exceptor.account_balance)
            self.make_withdrawl(amount)
            exceptor.make_deposit(amount)
            a_string="After transfer - User: %s's Balance: %d, Exceptor's User: %s's Balance: %d" \
                % (self.name, self.account_balance, exceptor.name, exceptor.account_balance)
            print(f"\n{b_string}\n{a_string}\n")
        else:
            print("Account balance $%d insufficient funds for transfer amount $%d" % (self.account_balance, amount) )
        return self

daniel=User("Daniel", "tandd2015@outlook.com")
harlow=User("Harlow", "tandd201@outlook.com")
christina=User("Christina", "tandd20@outlook.com")

daniel.make_deposit(50).make_deposit(50).make_deposit(50).make_withdrawl(5).display_user_balance()

harlow.make_deposit(75).make_deposit(70).make_withdrawl(25).make_withdrawl(20).display_user_balance()

christina.make_deposit(5000).make_withdrawl(1500).make_withdrawl(1500).make_withdrawl(1000).display_user_balance()

daniel.transfer_money(christina,5)