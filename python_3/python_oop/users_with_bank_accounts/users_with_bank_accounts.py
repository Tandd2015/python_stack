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

class User:
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.account={
            'checkings': BankAccount(),
            'savings': BankAccount()
        }
            
    
    def make_deposit(self, amount, dict_key):
        self.account['%s'%dict_key].deposit(amount)
        return self
    
    def make_withdrawl(self, amount, dict_key):
        self.account['%s'%dict_key].withdraw(amount)
        return self
    
    def display_user_balance(self, dict_key):
        print(f"User: {self.name} Balance: ${self.account['%s'%dict_key].balance}")
        return self

    def transfer_money(self,exceptor,amount,u_dict_key,e_dict_key):
        if amount<self.account['%s'%u_dict_key].balance:
            b_string="Before transfer - User: %s's Balance: %d, Exceptor's User: %s's Balance: %d" \
                %(self.name, self.account['%s'%u_dict_key].balance, exceptor.name, exceptor.account['%s'%e_dict_key].balance)
            self.account['%s'%u_dict_key].withdraw(amount)
            exceptor.account['%s'%e_dict_key].deposit(amount)
            a_string="After transfer - User: %s's Balance: %d, Exceptor's User: %s's Balance: %d" \
                % (self.name, self.account['%s'%u_dict_key].balance, exceptor.name, exceptor.account['%s'%e_dict_key].balance)
            print(f"\n{b_string}\n{a_string}\n")
        else:
            print("Account balance $%d insufficient funds for transfer amount $%d" % (self.account['%s'%u_dict_key].balance, amount) )
        return self

christina=User("Christina", "tandd20@outlook.com")
daniel=User("Daniel", "tandd2015@outlook.com")
daniel.make_deposit(50,'savings').make_deposit(50,'checkings').make_deposit(50,'checkings').make_withdrawl(5,'checkings').display_user_balance('checkings')
daniel.transfer_money(christina,5,'checkings','savings')