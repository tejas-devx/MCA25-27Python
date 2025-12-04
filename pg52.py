# Create a Bank account with members account number,name,type of account and balance.Write constructor and methods to deposit at the bank and withdraw an amount from the bank.

class Bank:
    def __init__(self, accno, name, acctype, balance):
        self.accno = accno
        self.name = name
        self.acctype = acctype
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt
        print("Deposited:", amt)

    def withdraw(self, amt):
        if amt > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amt
            print("Withdrawn:", amt)

    def display(self):
        print("\nAccount Details:")
        print("Account Number:", self.accno)
        print("Name:", self.name)
        print("Type:", self.acctype)
        print("Balance:", self.balance)


acc = int(input("Enter account number: "))
name = input("Enter name: ")
atype = input("Enter type of account: ")
bal = float(input("Enter opening balance: "))

b = Bank(acc, name, atype, bal)


dep = float(input("Enter amount to deposit: "))
b.deposit(dep)

wd = float(input("Enter amount to withdraw: "))
b.withdraw(wd)

b.display()