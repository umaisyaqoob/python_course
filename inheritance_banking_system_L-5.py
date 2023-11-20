class Account:
    def __init__(self, account_number, account_holder, balance):
        self._acc_num = account_number
        self.acc_hol = account_holder
        self.balance = balance

    def check_balance(self):
            return self.balance
    def deposit(self, amount):
             self.balance += amount
            
    def withdraw(self, amount):
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Balance insufficient")
    

class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
             return int(self.balance / 100 * self.interest_rate)

    def display_info(self):
            print(f"Account Number {self.acc_num}")
            print(f"Account Hoolder {self.acc_hol}")
            print(f"Balance : {self.balance}")
            print(f"Interest Rate: {self.interest_rate}%")
            print(f"Interest Earnd: {self.calculate_interest()}")


Acc = Account("792384", "Muhammad Umais", 10000)
acc_sav = SavingsAccount("792384", "Muhammad Umais", 10000, 5)
acc_sav.deposit(50000)
acc_sav.withdraw(1000)
acc_sav.display_info()


print(Acc._acc_num)