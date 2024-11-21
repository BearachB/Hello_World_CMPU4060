# Bearach Byrne - C15379616 - TU259
# Object Oriented Programming - Assignment 2 - 21/03/2021

# Imports time and string modules
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


# Defines the function that creates the dictionary of words and occurrences
def create_dict():
    # Opens the file
    file = open("ap_docs.txt", 'r')
    # Creates a blank dictionary
    article_dict = dict()
    article_number = 0
    num_list = []

    # Iterates through each line in the file
    for line in file:
        # Removes some of the formatting/misc characters from each line
        line = line.strip("\n")
        line = line.strip('.')
        line = line.strip(',')
        line = line.strip('')
        line = line.lower()

        # If it finds the new document line
        if line == "<new document>":
            # Increase doc num.
            article_number += 1

        # Otherwise, split each line into its component words
        else:
            line = line.split()
            # Iterates through each word in the line
            for word in line:
                # Strips punctuation from the words
                word = word.strip(string.punctuation)
                # If the word is already in the dictionary, add the current article index
                if word in article_dict:
                    article_dict[word].add(article_number)
                # Otherwise, add the word to the dict as key and article number as value
                else:
                    article_dict[word] = set(num_list)
                    article_dict[word].add(article_number)
    # Closes the file
    file.close()
    # Returns the dictionary containing the words and documents they show up in
    return article_dict


# Defines the search function
def search(create_dict):

    # The main function is inside a while loop so that it will keep prompting the user to search until they exit
    while True:

        # Takes in the user input, converts it to lower case, strips punctuation from it
        user_search = input("Enter any number of search terms to find articles that contain them all: ")
        user_search = user_search.lower()
        user_search = user_search.strip(string.punctuation)
        # This splits the input into a list which can be iterated through
        search_list = user_search.split()
        # Prints the number of search terms
        print("Number of search terms:", len(search_list), "\n")

        # If the search term is a single word, find the documents it appears in
        if len(search_list) == 1:
            word = search_list[0]
            # If it appears in the dictionary, print the values (i.e. document numbers)
            if word in create_dict:
                print("'", *search_list, "'", "Was found in article(s):", create_dict[word])
            # If it is not found, print the message
            else:
                print("Your word did not show up in any articles")

        # If the search term is longer than 1 term
        elif len(search_list) > 1:
            word_match = []
            control = True

            # Iterate through the list of search terms
            for word in search_list:
                # If the word is found, print where it occurs and add the list of documents it appears in to word_match
                if word in create_dict:
                    print("'", word, "'", "was found in article(s):", create_dict[word])
                    word_match.append(create_dict[word])
                    # Find common document numbers by checking the intersection of the sublists in word_match.
                    # A set is used to remove duplicates
                    common_articles = set(word_match[0]).intersection(*word_match)

                # If word not in the dictionary, print this to the user
                elif word not in create_dict:
                    print("'", word, "'", " did not show up in any articles")
                    # Set control_var to False if any of the search terms aren't in an article
                    control = False

            # If control var is False or the set is empty (this can happen if the set has been initialised in a run
            # and then the terms in a following run don't match). Print this to user
            if not control or len(common_articles) == 0:
                print("\nNo articles were found containing all of your words")
            else:
                print("\nYour words were found in the following article(s):", common_articles)

        # This is used to check if the user wants to exit
        user_confirm = input("\nDo you want to keep searching? (Y/N): ")
        if user_confirm == "N" or user_confirm == "n":
            print("Returning to main menu!")
            break


# This function creates the main menu that the user interacts with
def main_menu():

    # Some formatting to neaten the program up
    print("\n--------------------------- Program Start --------------------------")
    time.sleep(0.15)
    print("--------------------------- Introduction ---------------------------")
    time.sleep(0.15)
    print("Welcome to the Assignment 2 Python Script!\nPlease keep your hands and feet inside the program at all times. \nFollow the instructions and please try not to break the program!\n")

    # The while loop allows the user to do multiple operations without having to restart
    while True:

        # Prints formatting & instructions
        time.sleep(0.15)
        print("\nMAIN MENU")
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

        # Try clause used to make sure the user has entered a value that can be converted to an integer
        try:
            # Convert user value to an integer
            user_option = int(user_option)

            # If the user has chosen option 1, run the search function
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
