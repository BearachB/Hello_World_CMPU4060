class BankAccount():

    def __init__(self, iban, acc_no, funds, recent_trans):
        self.iban = iban
        self.acc_no = acc_no
        self.funds = funds
        self.recent_trans = recent_trans

    def deposit(self):
        amount = float(input("Enter an amount to be deposited: "))
        self.avail_funds += amount
        # if len(self.recent_trans) < 5:
        #     self.recent_trans.pop(0)
        print("Amount deposited: ", amount)

    def withdraw(self):
        amount = float(input("Enter an amount to be withdrawn: "))
        if self.avail_funds >= amount:
            self.avail_funds -= amount
            print("Amount withdrawn: ", amount)
        else:
            print("Insufficient Funds")

    def display(self):
        print("Account Number:", self.iban)
        print("Available Balance = ",self.avail_funds)


s = BankAccount("IE64IRCE92050112345678", "2275409", 1000, [])

s.deposit()
s.withdraw()
s.display()
