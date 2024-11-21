
# Creates the first function that takes the text file provided and populates
# a list with each document occupying 1 list item
def create_list():

    #Opens & reads the file
    my_file = open("ap_docs.txt", "r")
    file_read = my_file.read()
    #Creates a list split by the "<NEW DOCUMENT> headers
    paragraph_list = file_read.split("<NEW DOCUMENT>")
    #Removes the first item of the list (a blank item)
    paragraph_list.remove(paragraph_list[0])

    # Returns the document list
    return paragraph_list


# Creates the second function to enable the printing of specific articles
# This takes the list created in create_list as an input and prints whichever document the user wants
def print_article(create_list):
    # Tells the user the total number of documents to choose from
    print("There are",len(create_list),"documents to choose from.")
    # Creates an integer which takes the user input
    article_num = int(input("\nEnter a document number (1-226): "))
    # Prints the article the user selected
    print("\nDocument Number:",article_num)
    print("--------------------------------------------------------------------")
    print((create_list[article_num - 1]))
    print("\n--------------------------------------------------------------------")
    print("--------------------------------------------------------------------")



def create_dict():
    file = open("ap_docs.txt", 'r')
    article_dict = {}
    article_number = 0
    numList = []
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
                     article_dict[word] = set(numList)
                     article_dict[word].add(article_number)
    return article_dict


art_list = create_list()
art_dict = create_dict()

def search(create_dict):
    user_search = input("Enter any number of search terms to find articles that contain them all: ")
    user_search = user_search.lower()
    user_search = user_search.strip("'")
    user_search = user_search.strip('"')
    user_search = user_search.strip('.')
    user_search = user_search.strip(',')
    search_list = user_search.split()
    print("Number of search terms:",len(search_list))

    if len(search_list) == 1:
        word = search_list[0]
        print(word)
        if word in create_dict:
            print("'", *search_list, "'", "Was found in articles:", create_dict[word])
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
                print("'", word, "'"," did not show up in any articles")
                control = False

        if control == False:
            print("No articles were found containing all of your words")
        else:
            print("Your words were found in the following articles:", common_articles)
    return

def main_menu():
    control_var = 0
    print("Welcome to the Assignment 2 Python Script!\nPlease keep hands and feet inside the program at all times. \nFollow the instructions and try not to break the program!")
    while True:
        print("\n--------------------------------------------------------------------")
        print("What would you like to do?")
        print("1. Search for documents by keyword(s)")
        print("2. Read specific document")
        print("3. Quit")

        user_option = int(input("Enter a number (1-3): "))
        if user_option == 1:
            print("\n--------------------------------------------------------------------")
            search(create_dict())
            user_option = ""

        elif user_option == 2:
            print("\n--------------------------------------------------------------------")
            print_article(create_list())
            print("\n\n")
            user_option = ""

        elif user_option == 3:
            print("\n\n")
            print("--------------------------------------------------------------------")
            print("------------------------- Come back anytime ------------------------")
            print("---------------------------- Program End ---------------------------")
            break

main_menu()
