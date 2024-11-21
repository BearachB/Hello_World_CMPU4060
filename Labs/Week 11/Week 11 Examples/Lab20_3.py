class BankAccount(object):
    def __init__(self, name="", last_name="", address="", iban="", account_number=0, balance=0):
        self.__name = name
        self.__last_name = last_name
        self.__address = address
        self.__iban = iban
        self.__account_number = account_number
        self.__balance = balance
        self.__transactions = {}  # Dictionary to store all transactions. The key is the id of the transaction
        # The value is a tuple (a, b, c, d) where a is the value being deposited or
        # withdrawn, b is the type of transaction (deposit or withdraw), c is the balance after the transaction, and d
        # is a message the user can attached with the transaction
        # An example of 3 transactions from a initial balance of 100 could be:
        #  {1:(100, "deposit", 200, "salary"), 2:(55.60, "withdraw", 144.4, "electricity"), 3:(34, "withdraw", 110.4, "phone bill")}

        self.__transactions_count = 0  # A counter that needs to be incremented by 1 for each deposit or withdraw and
        # that is also used to identify a transaction

    def deposit(self, value, message):

        try:
            value = float(value)
        except ValueError:
            print("Value is not a number. Please pass a correct deposit value")
            return

        if value < 0:
            print("You cannot deposit a negative value")
            return

        self.__balance += value
        self.__transactions_count += 1
        self.__transactions.update({self.__transactions_count: (value, "deposit", self.__balance, message)})

    def withdraw(self, value, message):
        try:
            value = float(value)
        except ValueError:
            print("Value is not a number. Please pass a correct withdraw value")
            return

        if value < 0:
            print("You cannot withdraw a negative value")

        self.__balance -= value
        self.__transactions_count += 1
        self.__transactions.update({self.__transactions_count: (value, "withdraw", self.__balance, message)})

    def print_last_five_transactions(self):
        count = self.__transactions_count

        if count == 0:
            print("No transactions have been performed yet\n")
            return

        count_printed = 0
        while count > 0:
            count_printed += 1
            for key, value in self.__transactions.items():
                if key == count:
                    print("Transaction type:", value[1])
                    print("Value:", value[0])
                    print("Message:", value[3])
                    print("Balance:", value[2])
                    print()
                    break
            if count_printed == 5:
                break
            count -= 1

    def print_balance(self):
        print("Your current balance is", self.__balance)

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_value):
        self.__balance = new_value

    def get_transactions_count(self):
        return self.__transactions_count

    def set_transactions_count(self, new_value):
        self.__transactions_count = new_value

    def update_transactions(self, new_transactions):
        self.__transactions.update(new_transactions)

    # def __str__(self):
    #     pass


class MinimumBankAccount(BankAccount):
    def __init__(self, name="", last_name="", address="", iban="", account_number=0, balance=0, minimum_balance=0):
        BankAccount.__init__(self, name, last_name, address, iban, account_number, balance)
        self.__minimum_balance = minimum_balance

    def withdraw(self, value, message):

        try:
            value = float(value)
        except ValueError:
            print("Value is not a number. Please pass a correct withdraw value")
            return

        if value < 0:
            print("You cannot withdraw a negative value")
            return

        if self.get_balance() - value < self.__minimum_balance:
            print("Value to withdraw will result in a smaller value than the minimum balance allowed. Operation can not be concluded.")
            return

        self.set_balance(self.get_balance() - value)
        self.set_transactions_count(self.get_transactions_count() + 1)
        self.update_transactions({self.get_transactions_count(): (value, "withdraw", self.get_balance(), message)})


# # Lucas account with lots of money
lucas_account = MinimumBankAccount(name="Lucas", last_name="Rizzo", address="TUD", iban="IE12345789", balance=1000, minimum_balance=0)
lucas_account.print_last_five_transactions()
lucas_account.withdraw(100, "phone bill")
lucas_account.withdraw(300, "electricity")
lucas_account.withdraw(2000, "furniture")
lucas_account.print_last_five_transactions()
