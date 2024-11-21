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
    # The correct words will be appended to this list once they have been found
    results = []

    # The first for loop that iterates through the words list
    for word in words:

        m_count = 0
        # The second for loop iterates through the word one letter at a time
        for chars in word:
            # If there is one m in the word
            if "m" in chars:
                # Adds 1 to the m_count variable
                m_count += 1
                # If there is 2 ms, and all the other letters appear in the current word
                if m_count == 2 and "e" in word and "p" in word and "h" in word and "i" in word and "s" in word:
                    # Add word to results list
                    results.append(word)

    # Calculates how long the function took to run, rounded to 2 decimal places
    total_time  = round(time.process_time() - start_time,2)
    # Prints the time taken to run the function
    print("This function took",total_time, "seconds to run.")
    # Prints a statement saying how many words match
    print("There are", len(results), "words matching this criteria:")
    # Returns the results list
    return results


# Driver code to call the function and print the results
print(puzzle(get_word_list()))
