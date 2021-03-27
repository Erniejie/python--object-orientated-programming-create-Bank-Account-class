#Python-create Bank Account class
# Computer Programming Tutor_March 26,2021

class BankPro:
    def __init__(self):
        self.bal =0
        print("Welcome to the Deposit & Widthdrawal Matchine")

    def deposit(self):
        amount = float(input("Enter the Amount to be Deposited: "))
        self.bal +=amount
        print("\nAmount Deposited :",amount)

    def withdraw(self):
        amount = float(input("Enter the Amount to be Withdrawn: "))
        if self.bal >= amount:
            self.bal -=amount
            print("\nAmount Withdrawn=",amount)
        else:
            print("\nInsufficient Balance")
    def display(self):
        print("\n Account Balance=",self.bal)
        




#Creating an Object of Class
s = BankPro()

# Calling Functions with Class Object

s.deposit()
s.withdraw()
