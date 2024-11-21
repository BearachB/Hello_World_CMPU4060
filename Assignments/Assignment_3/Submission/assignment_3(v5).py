# Shopping Cart Class here:
class ShoppingCart(object):

    # The init method initialises the instance of the shopping cart class with 2 attributes;
    # the cart and the loyalty status
    def __init__(self, items={}, loyal=False):
        self.items = items
        self.loyal = loyal

    # The str method defined how an object of the shopping cart class will be printed
    # this is only printed upon the creation of a customer object
    def __str__(self):
        # Check if the cart is empty
        if self.items is None:
            return "Your cart is empty! Try adding some and then viewing."
        # If cart is not empty, print in the following format
        else:
            print("Items in cart: ")
            for key, value in self.items.items():
                return key, " : ", value

    # The add item method defines how an item is added to the user's cart
    def add_item(self, usr_add, usr_quant):
        # Takes the inputs for the what the user would like to add and how many
        usr_add = input("What item would you like to add?: ")
        usr_add_quant = int(input("How many?: "))
        # Creates the product dictionary using the populate dict function
        product_dict, product_dict_notobj = populate_dict(self.loyal)
        # If the input the user has entered is in the product list
        if usr_add in product_dict.keys():
            # If the product isn't already in the cart, add it to the cart
            if usr_add not in self.items.keys():
                self.items[usr_add] = usr_add_quant
                return self.items
            # If the product is already in the cart, add to the value
            else:
                self.items[usr_add] = self.items[usr_add] + usr_add_quant
                return self.items
        # If the input the user has entered isn't in the product list
        else:
            return "It looks like you entered an incorrect item name. Try viewing the product list again."

    # This rmeove item method defines how items are removed from the cart of the user
    def remove_item(self, usr_rem, usr_rem_quant):
        # Takes the inputs for the what the user would like to remove and how many
        usr_rem = input("What item would you like to remove?: ")
        usr_rem_quant = int(input("How many?: "))
        # Creates the product dictionary using the populate dict function
        product_dict, product_dict_notobj = populate_dict(self.loyal)
        # If the user input matches a product in the cart
        if usr_rem in self.items.keys():
            # If the number that the user wants to remove is greater than the number in the cart
            if usr_rem_quant > self.items[usr_rem]:
                print("Looks like you don't have that many in your cart")
            # Otherwise, if the number that the user wants to remove is less than the number in the cart
            elif usr_rem_quant == self.items[usr_rem]:
                del self.items[usr_rem]
            else:
                # Remove the number specified
                self.items[usr_rem] = self.items[usr_rem] - usr_rem_quant
                return self.items
        # If the item exists in the catalgue but not in the cart, tell that it's not in their cart
        elif usr_rem in product_dict.keys():
            return "It looks like that item isn't in your cart. Try again with an item that is."
        # Otherwise tell them that they have entered an invalid name
        else:
            return "It looks like you entered an incorrect item name."

    # This defines the method that prints out the contents of the user's cart
    def list_cart(self):
        # If the cart is not empty, print the contents line by line
        if bool(self.items):
            print("Items in cart: ")
            print("Item   :   Quantity")
            for key in self.items:
                print(key, "    :    ", self.items[key])
        else:
            print("There's nothing in your cart yet! Try adding something and coming back here!")

    # Defines the checkout method
    def checkout(self):
        subtotal = 0.0
        checkout_list_yes = ["y", "ye", "yes"]
        checkout_list_no = ["n", "no"]
        checkout_list = checkout_list_yes + checkout_list_no
        product_dict, product_dict_notobj = populate_dict(self.loyal)
        # If the cart has items in it
        if bool(self.items):
            # For each item in the shopping cart dict, calculate the subtotal and add it to the subtotal to be printed
            for key in self.items:
                quant = int(self.items[key])
                price = product_dict_notobj[key]
                item_total = float(quant * price)
                subtotal += item_total
                subtotal_str = "€"
                subtotal_str += str(subtotal)
            self.list_cart()
            print("Your subtotal is:", subtotal_str)
            print("\n--------------------------------------------------------------------")

            # If the customer is loyal (checked by checking the loyaly status of their cart which is set depending on
            # the user's class (LoyalCust or Bargain Hunter) and their purchase is above €200, give them a 5% discount
            if self.loyal is True and subtotal > 200.0:
                print("Because of your loyalty status, you also get a 5% discount on this purchase as it is over €200")
                discount = 0.05
                subtotal = subtotal * (1.0 - discount)
                subtotal = round(subtotal, 2)
                subtotal_str = "€"
                subtotal_str += str(subtotal)
                print("This brings your total to:", subtotal_str)
            # If the user is loyal but their purchase is under €200, tell them how much they need to add to their cart
            # to avail of the discount
            elif self.loyal is True and subtotal < 200.0:
                print("Because of your loyalty status, you are eligible for a 5% discount on purchases over €200")
                discount_threshold = 200 - subtotal
                print("Add a further €", discount_threshold, "worth of items to your cart to avail of this discount!")
            # Input asking if they want to continue
            checkout_control = input("Do you want to proceed with checkout? (Y/N): ").lower()
            # Keep asking for an answer until they provide a yes or no
            while checkout_control not in checkout_list:
                print("Looks like you entered an invalid character! Try again.")
                checkout_control = input("Do you want to proceed with checkout? (Y/N): ").lower()

            # If the user chooses to checkout print a thank you message, clear their cart and then end the program
            if checkout_control in checkout_list_yes:
                self.items.clear()
                print("Thank you for your purchase!")

            # If the user chooses to not check out
            elif checkout_control in checkout_list_no:
                print("You have chosen to return to the menu")
        # Otherwise, when there is nothing in the cart
        else:
            print("There's nothing in your cart yet! Try adding something and coming back here!")


# Product Class here:
class Product(object):
    instances = []

    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price
        self.__class__.instances.append(self)

    def __str__(self):
        return "\nProduct Name: {}\nProduct Price: €{}".format(self.product_name, self.product_price) + "\n" + "-" * 20 + "\n"

    # Method to allow the price of an item to be changed. This was not fully implemented in the end.
    def change_price(self, new_price):
        self.price = str(new_price)
        return self.price


# Customer Class here:
class Customer(object):
    def __init__(self, usr_id, name: str, dob: str, email: str, phone: str, cart=None):
        self.usr_id = usr_id
        self.name = name
        self.dob = dob
        self.email = email
        self.phone = phone
        self.cart = ShoppingCart({}, cart)

    def __str__(self):
        table_head = "-" * 100 + "\n"
        table_head += "ID:" + " | "
        table_head += "Name: " + " " * 7 + " | "
        table_head += "DOB: " + " " * 5 + " | "
        table_head += "Email: " + " " * 15 + " | "
        table_head += "Phone: " + " " * 3 + " | "
        print(table_head)

        cust_str = "-" * 100 + "\n"
        cust_str += str(self.usr_id) + " " * 2 + " | "
        cust_str += str(self.name) + " | "
        cust_str += str(self.dob) + " | "
        cust_str += str(self.email) + " | "
        cust_str += str(self.phone) + " | " + "\n"
        return cust_str


# Loyal Customer Subclass here:
class LoyalCustomer(Customer):
    def __init__(self, usr_id, name: str, dob: str, email: str, phone: str, cart=None, loyal=True):
        super().__init__(usr_id, name, dob, email, phone, cart)
        self.loyal = loyal

    def __str__(self):
        table_head = "-" * 100 + "\n"
        table_head += "ID:" + " | "
        table_head += "Name: " + " " * 7 + " | "
        table_head += "DOB: " + " " * 5 + " | "
        table_head += "Email: " + " " * 15 + " | "
        table_head += "Phone: " + " " * 3 + " | "
        table_head += "Loyal: " + " " * 3 + " | "
        print(table_head)

        cust_str = "-" * 100 + "\n"
        cust_str += str(self.usr_id) + " " * 2 + " | "
        cust_str += str(self.name) + " | "
        cust_str += str(self.dob) + " | "
        cust_str += str(self.email) + " | "
        cust_str += str(self.phone) + " | "
        cust_str += str(self.loyal) + " | " + "\n"
        return cust_str


# Bargain Hunter Subclass here:
class BargainHunter(Customer):
    def __init__(self, usr_id, name: str, dob: str, email: str, phone: str, cart=None, loyal=False):
        super().__init__(usr_id, name, dob, email, phone, cart)
        self.loyal = loyal

    def __str__(self):
        table_head = "-" * 100 + "\n"
        table_head += "ID:" + " | "
        table_head += "Name: " + " " * 7 + " | "
        table_head += "DOB: " + " " * 5 + " | "
        table_head += "Email: " + " " * 15 + " | "
        table_head += "Phone: " + " " * 3 + " | "
        table_head += "Loyal: " + " " * 3 + " | "
        print(table_head)

        cust_str = "-" * 100 + "\n"
        cust_str += str(self.usr_id) + " " * 2 + " | "
        cust_str += str(self.name) + " | "
        cust_str += str(self.dob) + " | "
        cust_str += str(self.email) + " | "
        cust_str += str(self.phone) + " | "
        cust_str += str(self.loyal) + " | " + "\n"
        return cust_str


# This function creates the main menu that the user interacts with
def main_menu():
    # Some formatting to neaten the program up
    print("\n--------------------------- Program Start --------------------------")
    print("--------------------------- Introduction ---------------------------")
    print()
    print("Welcome to the Assignment 3 Python Script!\n")

    # The while loop allows the user to do multiple operations without having to restart
    option1_check = 0
    user_option = 0
    while user_option != 6:

        # Prints formatting & instructions
        print("\nMAIN MENU")
        print("-" * 50 + "\n")
        print("What would you like to do?\n")
        print("1. Create a Customer")
        print("2. List available products")
        print("3. Add/Remove a product to the shopping cart")
        print("4. See current shopping cart")
        print("5. Checkout")
        print("6. Quit \n")

        # Variable that takes the user input
        user_option = input("Enter a number (1-6): ")

        # Try clause used to make sure the user has entered a value that can be converted to an integer
        try:
            # Convert user value to an integer
            user_option = int(user_option)

            # If the user has chosen option 1, they want to create a new user
            if user_option == 1:
                print("-" * 50)
                print("\nCREATE CUSTOMER SUBMENU")
                print("-" * 50 + "\n")
                print("We're going to need some information to create your account. \n")

                # Calls the relevant function to validate the user input for each field
                user_name1 = usr_input_name1()
                user_name2 = usr_input_name2()
                user_dob = usr_input_dob()
                user_email = usr_input_email()
                user_number = usr_input_phone()

                user_name = user_name2 + "." + user_name1
                # Create an instance of the Customer superclass for this user
                cust = Customer(1, user_name, user_dob, user_email, user_number, {})
                # Creates variables used for checking the user input
                loyal_or_bargain = ""
                loyal_or_bargain_list_yes = ["y", "ye", "yes"]
                loyal_or_bargain_list_no = ["n", "no"]
                loyal_or_bargain_list = loyal_or_bargain_list_yes + loyal_or_bargain_list_no
                while loyal_or_bargain not in loyal_or_bargain_list:
                    loyal_or_bargain = input("Do you want to join our loyalty programme to get access to exclusive deals and products? (Y/N): ").lower()
                    # If they have selected yes
                    if loyal_or_bargain in loyal_or_bargain_list_yes:
                        # Creates a loyal customer and populates the loyal dictionary from the external txt file
                        cust = LoyalCustomer(1, user_name, user_dob, user_email, user_number, {}, loyal=True)
                        product_dict, product_dict_notobj = populate_dict(True)
                        cust_cart = ShoppingCart({}, True)
                        break
                    # Otherwise, if they select no
                    elif loyal_or_bargain in loyal_or_bargain_list_no:
                        # Creates a bargain hunter and populates the loyal dictionary from the external txt file
                        cust = BargainHunter(1, user_name, user_dob, user_email, user_number, {}, loyal=False)
                        product_dict, product_dict_notobj = populate_dict(False)
                        cust_cart = ShoppingCart({}, False)
                        break
                    # If the user enters anything else
                    else:
                        print("Looks like you entered an invalid input")
                option1_check = 1
                print(cust)

            if option1_check == 1:
                # If the user chooses option 2, run the print_article function that allows them to
                # print a single article at a time
                if user_option == 2:
                    print("\n--------------------------------------------------------------------")
                    print("You have chosen to list the products")
                    list_products(product_dict)


                elif user_option == 3:
                    user_add_rem = 0
                    while user_add_rem != 3:
                        print("\n--------------------------------------------------------------------")
                        print("You have chosen to add or remove an item from the cart.")
                        print("1. To add item to cart")
                        print("2. To remove item from cart")
                        print("3. To exit to main menu")
                        user_add_rem = int(input("Enter your selection (1 - 3): "))

                        if user_add_rem == 1:
                            print(cust_cart.add_item(product_dict, cust_cart))

                        elif user_add_rem == 2:
                            print(cust_cart.remove_item(product_dict, cust_cart))

                        elif user_add_rem == 3:
                            break

                # If the user chooses option 4
                elif user_option == 4:
                    print("\n--------------------------------------------------------------------")
                    print("You have chosen to print your current cart\n")
                    cust_cart.list_cart()

                # If the user chooses option 5, run the checkout method
                elif user_option == 5:
                    print("\n--------------------------------------------------------------------")
                    print("You have chosen to checkout\n")
                    cust_cart.checkout()

                    # This checks whether the cart is empty after the checkout has been run. If it is not empty it
                    # brings the user back to the menu. If it is empty, the user has chosen to checkout and the program
                    # ends
                    if not bool(cust_cart.items):
                        user_option = 6

            # If the user tries to select any option other 1 before making an account it will tell them to make
            # one first
            elif user_option == 2 or user_option == 3 or user_option == 4 or user_option == 5:
                print("\nYou must create a customer before performing any account options!")
                print("-" * 100 + "\n")

            # If the user chooses to quit, print a message
            elif user_option == 6:
                print("You have chosen to quit")

            # Else (i.e. if the user enters a number that isn't 1-6, print a warning message
            else:
                print("--------------------------------------------------------------------")
                print("\nLooks like you've entered an invalid number. Try entering  1-6!\n")

        # Accounts for invalid inputs such as strings or misc. characters
        except ValueError:
            print("\n--------------------------------------------------------------------")
            print("Looks like you've entered an illegal input. Try entering a valid number!\n")

    # End program message
    print("\n\n")
    print("------------------------Thanks For Your Time------------------------")
    print("------------------------- Come Back Anytime ------------------------")
    print("---------------------------- Program End ---------------------------")
    print("--------------------------------------------------------------------")


# This populates the product dictionary based off the contents of "item_list.txt"
def populate_dict(loyal):
    # Opens the file created for this assignment that provides the items
    my_file = open("item_list.txt", "r")
    line_list = []
    my_dict = {}
    product_dict = {}
    # If the user is a loyal customer, add all items to the dict
    if loyal:
        for line in my_file:
            line = line.strip("\n")
            line_list.append(line.split(" "))
        for elem in line_list:
            my_dict[elem[0]] = float(elem[1])
        # Sorts the dict into descending price using a lambda function
        sorted_dict = dict(sorted(my_dict.items(), key=lambda kv: kv[1], reverse=True))
    # If the user is a bargain hunter, don't add the loyal exclusives to the list
    else:
        for line in my_file:
            line = line.strip("\n")
            line_list.append(line.split(" "))
        for elem in line_list:
            if len(elem) == 2:
                my_dict[elem[0]] = float(elem[1])
        # Sorts the dict into ascending price using a lambda function
        sorted_dict = dict(sorted(my_dict.items(), key=lambda kv: kv[1], reverse=False))

    # Creates an instance of the product class for each product in the sorted dictionary
    for item in sorted_dict:
        product_dict[item] = Product(item, my_dict[item])
    my_file.close()
    return product_dict, sorted_dict

# This function is used to print the products
def list_products(prod_dict):
    product_num = 1
    for key, value in prod_dict.items():
        print("Product Number:", product_num)
        product_num += 1
        print(value)

# This function defines the user input for their first name
def usr_input_name1():
    while True:
        user_name1 = input("Enter your first name: ").lower()
        try:
            if user_name1.isalpha():
                return user_name1
        except ValueError:
            print("Looks like you've entered an illegal input. Try entering a name that only has letters in it")
        else:
            print("Looks like you've entered an illegal input. Try entering a name that only has letters in it")

# This function defines the user input for their last name
def usr_input_name2():
    while True:
        user_name1 = input("Enter your last name: ").lower()
        try:
            if user_name1.isalpha():
                return user_name1
        except ValueError:
            print("Looks like you've entered an illegal input. Try entering a name that only has letters in it")
        else:
            print("Looks like you've entered an illegal input. Try entering a name that only has letters in it")


# This function defines the user input for their dat of birth
def usr_input_dob():
    while True:
        user_dob = input("Enter your DOB in the format 'dd/mm/yyyy' : ")
        try:
            if len(user_dob) == 10:
                return user_dob
        except ValueError:
            print("Looks like you've entered an illegal input. Try entering a DOB")
        else:
            print("Looks like you've entered an illegal input. Try entering a date in the format dd/mm/yyyy")


# This function defines the user input for their email address
def usr_input_email():
    while True:
        user_email = input("Enter your email address: ").lower()
        try:
            if "@" in user_email and "." in user_email:
                return user_email
        except ValueError:
            print("Looks like you've entered an illegal input. Try entering a valid email address")
        else:
            print("Looks like you've entered an illegal input. Try entering an email address in the form 'x@website.com")


# This function defines the user input for their phone number
def usr_input_phone():
    while True:
        user_number = (input("Enter your phone number: "))
        try:
            if user_number.isnumeric() and len(user_number) == 10:
                return user_number
        except ValueError:
            print("Looks like you've entered an illegal input. Try entering a valid email address")
        else:
            print("Looks like you've entered an illegal input. Try entering a 10 digit mobile number without any spaces"
                  " in the form 08XXXXXXXX")

# Defines the testing function to show the loyal customer process
# It should be noted that error checking is not implemented properly on this test function, so any inputs that need to
# be added should exactly match the prompt given
def testLoyal():
    print("Creating Customer Object\n")
    test_cust = Customer(1, "Byrne.Bearach", "06/11/1996", "bearachbyrne@gmail.com", "0864599537", {})
    print(test_cust)
    print("Creating Loyal Customer\n")
    test_cust = LoyalCustomer(1, "Byrne.Bearach", "06/11/1996", "bearachbyrne@gmail.com", "0864599537", {}, loyal=True)
    print(test_cust)
    product_dict, product_dict_notobj = populate_dict(True)
    cust_cart = ShoppingCart({}, True)
    print("Listing the products available:\n")
    list_products(product_dict)
    print("Adding an item to the cart!\n")
    print("INSTRUCTION: Enter 'pc' at first prompt and '5' at the second to add 1 PC to the cart")
    print(cust_cart.add_item(product_dict, cust_cart))
    print("Removing an item from the cart!\n")
    print("INSTRUCTION: Enter 'pc' at first prompt and '1' at the second to remove 1 PC from the cart")
    print(cust_cart.remove_item(product_dict, cust_cart))
    print("\nYou have chosen to print your current cart\n")
    cust_cart.list_cart()
    print("INSTRUCTION: Enter 'y' to complete the checkout")
    print("You have chosen to checkout\n")
    cust_cart.checkout()


# Defines the testing function to show the bargain hunter process
# It should be noted that error checking is not implemented properly on this test function, so any inputs that need to
# be added should exactly match the prompt given
def testBargain():
    print("Creating Customer Object\n")
    test_cust = Customer(1, "Byrne.Bearach", "06/11/1996", "bearachbyrne@gmail.com", "0864599537", {})
    print(test_cust)
    print("Creating Loyal Customer\n")
    test_cust = BargainHunter(1, "Byrne.Bearach", "06/11/1996", "bearachbyrne@gmail.com", "0864599537", {}, loyal=False)
    print(test_cust)
    product_dict, product_dict_notobj = populate_dict(False)
    cust_cart = ShoppingCart({}, False)
    print("Listing the products available:\n")
    list_products(product_dict)
    print("Adding an item to the cart!\n")
    print("INSTRUCTION: Enter 'pc' at first prompt and '5' at the second to add 1 PC to the cart")
    print(cust_cart.add_item(product_dict, cust_cart))
    print("Removing an item from the cart!\n")
    print("INSTRUCTION: Enter 'pc' at first prompt and '1' at the second to remove 1 PC from the cart")
    print(cust_cart.remove_item(product_dict, cust_cart))
    print("\nYou have chosen to print your current cart\n")
    cust_cart.list_cart()
    print("INSTRUCTION: Enter 'y' to complete the checkout")
    print("You have chosen to checkout\n")
    cust_cart.checkout()


# This calls the loyal test function
# testLoyal()

# This calls the bargain hunter test function
# testBargain()

# Driver code to call the main menu function
main_menu()
