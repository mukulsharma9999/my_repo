class BankAccount:
    def __init__(self,account_number, account_holder, balance=0):
        self.account_number = account_holder
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self,ammount):
        self.balance+=ammount
        print(f"Deposited :{ammount}")
        print(f"New balance :{self.balance}")


    def withdraw(self,ammount):
        if ammount<=self.balance:
            self.balance-=ammount
0            print(f"Withdrew  :{ammount}")
            print(f"New balance : {self.balance}")
        else:
            print("Insufficient funds")


    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder:{self.account_holder}"
bank_check = BankAccount(1234,"mukul",1000)
print(bank_check.deposit(23))
print(bank_check.withdraw(24))
