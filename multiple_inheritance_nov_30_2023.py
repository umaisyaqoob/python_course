class Bank:
    def __init__(self, name):
        self.bank_name = name
    
    def name(self):
        return f"Bank is {self.bank_name}"

class Accounts(Bank):
    def __init__(self, name, assets, liabilities, expense, income, capital):
        super().__init__(name)    
        self.assets = assets
        self.liabilities = liabilities
        self.expense = expense
        self.income = income
        self.capital = capital

    def assete_m(self):
        return f"This is {self.assets} Account"
    
    def liabilities_m(self):
        return f"This is {self.liabilities} Account"
    
    def expense_m(self):
        return f"This is {self.expense} Account"
    
    def income_m(self):
        return f"This is {self.income} Account"
    
    def capital_m(self):
        return f"This is {self.capital} Account"
    

class Management(Bank):
    def __init__(self, name, hr, assistant_hr):
        super().__init__(name)
        self.hr = hr
        self.assistant_hr = assistant_hr

    def info(self):
        return f"Hr name is {self.hr} and assistant HR is {self.assistant_hr} of {self.name()}"
    

class Dog(Bank):
    def dname(self):
        return f"Dog {self.bank_name}"
    
class Cat(Bank):
    def cname(self):
        return f"Cat {self.bank_name}"

class BankDetail(Dog, Cat):
   pass


bank = Bank("HBL")
accounts = Accounts("HBL" , "Assets", "Liabilities", "Expense", "Income", "Capital")
management = Management("HBL" , "Zunair", "Rustam")
bank_detail = BankDetail("Equal")
print(accounts.name())
print(accounts.assete_m())
print(accounts.liabilities_m())
print(accounts.expense_m())
print(accounts.income_m())
print(accounts.capital_m())
print(management.info())
print(bank_detail.dname())
print(bank_detail.cname())