#Get word function goes here to generate the list of words.
def get_word_list():
   """ Return a list of words from a word_list.txt file. """
   data_file = open("word_list.txt", "r")
   word_list = []  # start with an empty word list
   for word in data_file:  # for every word (line) in the file
       # strip off end−of−line characters and make each word lowercase
       # then append the word to the word list
       word_list.append(word.strip().lower())
   return word_list

# Definition of the new function 'puzzle'. This function takes 1 argument (words).
# The function will take the list of 45,000 words provided and return a list of words matching the criteria.
def puzzle(words):
    # Imports the time module so that the function can be timed to assess efficiency
    import time
    # Sets the start time
    start_time = time.process_time()
    # The characters we are looking for
    search = "lmnopqrstuv"
    # The matching words will be appended to this list once they have been found
    results = []

    # The first for loop that iterates through the list of 45,000 words
    for word in words:
        # The count used to check how many matching characters a word has
        count = 0

        # The second for loop that is used to check the contents of individual letters within the words
        for letter in search:
            # The if statement uses the find function to check if the letter contains a letter from the list
            # If result of find is not equal to -1 (i.e. it has found a match)
            if word.find(letter) != -1:
                # Adds 1 to the count variable to keep track of how many words from our list have been used
                count +=1
            # If the word isn't already in the lsit and the count is equal to 9
            if results.count(word) < 1 and count == 9:
                # Append given word to results list
                results.append(word)

    # Calculates how long the function took to run, rounded to 2 decimal places
    total_time  = round(time.process_time() - start_time,2)
    # Prints the time taken to run the function
    print("This function took",total_time, "seconds to run.")
    # Prints a statement saying how many words match the criteria
    print("There are", len(results), "words matching this criteria:")
    # Returns the results list
    return results


# Driver code to call the function and print the results
print(puzzle(get_word_list()))
