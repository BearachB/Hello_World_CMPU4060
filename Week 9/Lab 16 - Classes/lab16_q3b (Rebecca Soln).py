class BankAccount():
# CLASS OBJECT ATTRIBUTES
    def __init__(self, iban, acc_no, avail_funds, last5trans_list, withdraw_amt, deposit_amt):
        self.iban = iban
        self.acc_no = acc_no
        self.avail_funds = avail_funds
        self.last5trans_list = last5trans_list
        self.withdraw_amt = withdraw_amt
        self.deposit_amt = deposit_amt
# METHOD
    def withdraw(self):
        self.avail_funds = self.avail_funds - self.withdraw_amt
        self.withdraw_amt = - self.withdraw_amt
        self.last5trans_list.insert(0, self.withdraw_amt)
        self.last5trans_list.pop()
        return print("You have withdrawn: ", self.withdraw_amt, ". Your new balance is: ", self.avail_funds)
    def deposit(self):
        self.avail_funds = self.avail_funds + self.deposit_amt
        self.last5trans_list.insert(0, self.deposit_amt)
        self.last5trans_list.pop()
        return print("You have deposited: ", self.deposit_amt, ". Your new balance is: ", self.avail_funds)
    def show_last5transactions(self):
        return self.last5trans_list

s = BankAccount(self,"IE64IRCE92050112345678", "56130245", [], 0, 0)

s.deposit()
s.withdraw()
s.show_last5transactions()
