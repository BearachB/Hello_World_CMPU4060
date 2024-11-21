class BankAccount:
    def __init__(self, iban, account_number, funds, last_five_transactions):
        self.iban = iban
        self.account_number = account_number
        self.funds = funds
        self.transactions = last_five_transactions
    def withdraw(self, withdraw_amount):
        if int(withdraw_amount) > self.funds:
            print("Insufficient Funds, try a different amount.")
        else:
            self.funds = self.funds - int(withdraw_amount)
            self.transactions.append(-int(withdraw_amount))
            if len(self.transactions) == 6:
                self.transactions.pop(0)
            print("You have withdrawn", str(withdraw_amount), ". There is", str(self.funds), "remaining.")
    def deposit(self, deposit_amount):
        self.funds = self.funds + int(deposit_amount)
        self.transactions.append(int(deposit_amount))
        if len(self.transactions) == 6:
            self.transactions.pop(0)
        print("You have withdrawn", str(deposit_amount), ". There is", str(self.funds), "remaining.")
    def __str__(self):
        return "Account number " + self.account_number + " has " + str(self.funds)

p1 = BankAccount("IB120334023545", "10456585", 100001, [])
while True:
    our_input = input("What would you like to do?\n"
                  "1 Withdraw\n"
                  "2 Deposit\n"
                  "3 View Funds\n"
                  "4 View last 5 transactions\n"
                  "Exit (any other input)\n"
                  ">")
    if our_input == "1":
        withdraw_amount = input("Please input an amount to withdraw: ")
        p1.withdraw(withdraw_amount)
        click_enter = input("Please click enter to continue. ")
    elif our_input == "2":
        deposit_amount = input("Please input an amount to deposit: ")
        p1.deposit(deposit_amount)
        click_enter = input("Please click enter to continue. ")
    elif our_input == "3":
        print(p1)
        click_enter = input("Please click enter to continue. ")
    elif our_input == "4":
        print(p1.transactions)
        click_enter = input("Please click enter to continue. ")
    else:
        exit()
