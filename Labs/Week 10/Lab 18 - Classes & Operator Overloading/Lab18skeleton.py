#!/usr/bin/python3

# Use the https://exchangerate.host/ to perform currency conversions.
# https://api.exchangerate.host/convert?from=USD&to=EUR

import urllib.request
import json

class Currency:
    """INSERT A DOC STRING HERE"""

    VALID_CURRENCIES = ['USD', 'EUR', 'GBP', 'AUD', 'CAD',
                        'CNY', 'ILS', 'MXN', 'RUB', 'THB', 'BRL']

    def __init__(self, amount=1, currency_type='USD'):
        # a quick way of checking for valid currencies
        # for a limited subset of valid currencies
        if currency_type in Currency.VALID_CURRENCIES:
            self.amount = amount
            self.currency_type = currency_type
        else:
            print("Invalid currency type: %s\n", currency_type)
            self.amount = 0
            self.currency_type = ''

    def convert_to(self, new_currency_type: str):

        if new_currency_type == self.currency_type:
            return Currency(self.amount, self.currency_type)

        if new_currency_type not in Currency.VALID_CURRENCIES \
                or self.currency_type not in Currency.VALID_CURRENCIES:
            print("Conversion from {} to {} not allowed".format(self.currency_type, new_currency_type))
            return
        else:
            url = "https://api.exchangerate.host/convert?from="
            url += self.currency_type
            url += "&to=" + new_currency_type
            print(url)
            conv = urllib.request.urlopen(url)
            # read() returns an array of bytes, we want a string decoded in UTF-8
            response = conv.read().decode('UTF-8')
            info_rate = json.loads(response)
            rate = info_rate["result"]
            result = rate * self

            result = self.amount * info_rate["result"]

            return Currency(result)
            print(response)

            # Extract the exchange rate from the variable 'response' and finish the implementation of the method.
            # The return is given. amount is the the correct converted amount that needs to be found

            print("{} {} => {} {}".format(self.amount, self.currency_type, amount, new_currency_type))
            return Currency(amount, new_currency_type)

    def __str__(self):
        return("The amount is", str(self.amount), "in", self.currency_type)

    def __repr__(self):
        pass

    def __add__(self, other_curr):

        if type(other_curr) == int or type(other_curr) == float:
            other_curr = Currency(other_curr, self.currency_type)

        if self.currency_type != other_curr.currency_type:
            new_amount = self.amount + other_curr.convert_to(self.currency_type)
            return Currency(new_amount, self.currency_type)

        else:
            new_amount =

    def __sub__(self, other_curr):
        pass

    def __radd__(self, other_curr):
        return self.__add__()

    def __rsub__(self, other_curr):
        pass

    def __gt__(self, other_curr):
        pass


# This main is incomplete because not all methods are tested
# Some outputs are given by the comments next to the commands. Your code should be able to output these when
# you remove the '#' in the beginning of the lines

curr = Currency(7.50, 'USD')
curr2 = Currency(2, 'EUR')

new_curr = curr2.convert_to(curr.currency_type)  # 2.000000 EUR => 2.211600 USD
# print(curr) # 7.50 USD
# curr2 = Currency(2, 'EUR')
curr3 = curr + curr2
print(curr3)

# print(curr2)  # 2.00 EUR
# new_curr = curr2.convert_to(curr.currency_type) # 2.000000 EUR => 2.211600 USD
# print(new_curr) # 2.21 USD
# sum_curr = curr + curr2 # 2.000000 EUR => 2.211600 USD
# print(sum_curr) # 9.71 USD
# sum_curr2 = curr + 5.5
# print(sum_curr2) # 13.00 USD
