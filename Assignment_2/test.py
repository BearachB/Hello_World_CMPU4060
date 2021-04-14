import time
import string


# Creates the first function that takes the text file provided and populates
# a list with each document occupying 1 list item
def create_list():

    # Opens & reads the file
    my_file = open("ap_docs.txt", "r")
    file_read = my_file.read()

    # Creates a list split by the "<NEW DOCUMENT> headers
    paragraph_list = file_read.split("<NEW DOCUMENT>")
    # Removes the first item of the list (a blank item)
    paragraph_list.remove(paragraph_list[0])

    # Closes te file
    my_file.close()

    # Returns the document list
    return paragraph_list


# Creates the second function to enable the printing of specific articles
# This takes the list created in create_list as an input and prints whichever document the user wants
def print_article(create_list):
    while True:
        # Tells the user the total number of documents to choose from
        print("There are", len(create_list), "documents to choose from.")
        # Creates an integer which takes the user input
        article_num = int(input("\nEnter a document number (1-226): "))
        try:
            # Prints the article the user selected
            print("\nDocument Number:", article_num)
            print("--------------------------------------------------------------------")
            print((create_list[article_num - 1]))
            print("--------------------------------------------------------------------")
        except IndexError:
            print("You entered an invalid article number!")
        except ValueError:
            print("You entered an invalid character!")
        user_confirm = input("\nDo you want to keep printing specific articles? (Y/N): ")
        if user_confirm == "N" or user_confirm == "n":
            print("Returning to main menu!")
            break


def create_dict():
    file = open("ap_docs.txt", 'r')
    article_dict = {}
    article_number = 0
    num_list = []
    for line in file:
        line = line.strip("\n")
        line = line.strip('.')
        line = line.strip(',')
        line = line.strip('')
        line = line.lower()
        if line == "<new document>":
            article_number += 1
        else:
            line = line.split()
            for word in line:
                if word in article_dict:
                    article_dict[word].add(article_number)
                else:
                    article_dict[word] = set(num_list)
                    article_dict[word].add(article_number)
    # Closes the file
    file.close()
    # Returns the dictionary containing the words and documents they show up in
    return article_dict


# Defines the search function which will be used
def search(create_dict):
    while True:
        user_search = input("Enter any number of search terms to find articles that contain them all: ")
        user_search = user_search.lower()
        user_search = user_search.strip("'")
        user_search = user_search.strip('"')
        user_search = user_search.strip('.')
        user_search = user_search.strip(',')
        user_search = user_search.strip(string.punctuation)
        search_list = user_search.split()
        print("Number of search terms:", len(search_list), "\n")
        if len(search_list) == 1:
            word = search_list[0]
            if word in create_dict:
                print("'", *search_list, "'", "Was found in article(s):", create_dict[word])
            else:
                print("Your word did not show up in any articles")

        elif len(search_list) > 1:
            word_match = []
            control = True
            for word in search_list:
                if word in create_dict:
                    print("'", word, "'", "was found in articles:", create_dict[word])
                    word_match.append(create_dict[word])
                    common_articles = set(word_match[0]).intersection(*word_match)

                elif word not in create_dict:
                    print("'", word, "'", " did not show up in any articles")
                    control = False

            if not control:
                print("\nNo articles were found containing all of your words")
            else:
                print("\nYour words were found in the following articles:", common_articles)

        user_confirm = input("\nDo you want to keep searching? (Y/N): ")
        if user_confirm == "N" or user_confirm == "n":
            print("Returning to main menu!")
            break

    return


# This function creates the main menu that the user interacts with
def main_menu():
    # Some formatting to neaten the program up
    print("\n--------------------------- Program Start --------------------------")
    time.sleep(0.4)
    print("--------------------------- Introduction ---------------------------")
    time.sleep(0.4)
    print("Welcome to the Assignment 2 Python Script!\nPlease keep your hands and feet inside the program at all times. \nFollow the instructions and please try not to break the program!\n")
    # The while loop allows the user to do multiple operations without having to restart
    while True:
        # Prints formatting & instructions
        time.sleep(0.4)
        print("MAIN MENU")
        print("--------------------------------------------------------------------")
        time.sleep(0.15)
        print("What would you like to do?\n")
        time.sleep(0.15)
        print("1. Search for documents by keyword(s)")
        time.sleep(0.15)
        print("2. Read specific document")
        time.sleep(0.15)
        print("3. Quit")
        time.sleep(0.15)

        # Variable that takes the user input
        user_option = input("Enter a number (1-3): ")

        try:
            user_option = int(user_option)
            if user_option == 1:
                print("\n--------------------------------------------------------------------")
                search(create_dict())
                time.sleep(1)

            # If the user chooses option 2, run the print_article function that allows them to
            # print a single article at a time
            elif user_option == 2:
                print("\n--------------------------------------------------------------------")
                print_article(create_list())
                print("\n\n")
                time.sleep(1)

            # If the user chooses option 3, print an ending message and quite the program
            elif user_option == 3:
                print("\n\n")
                print("------------------------Thanks For Your Time------------------------")
                print("------------------------- Come Back Anytime ------------------------")
                print("---------------------------- Program End ---------------------------")
                print("--------------------------------------------------------------------")
                break

            # Else (i.e. if the user enters a number that isn't 1,2 or 3), print a warning message
            else:
                print("--------------------------------------------------------------------")
                print("\nLooks like you've entered an invalid number. Try entering  1, 2, or 3!\n")
                time.sleep(1)

        # Accounts for invalid inputs such as strings or misc. characters
        except ValueError:
            print("\n--------------------------------------------------------------------")
            print("Looks like you've entered an illegal input. Try entering a valid number!\n")
            time.sleep(1)


# Driver code to call the main menu function
main_menu()
