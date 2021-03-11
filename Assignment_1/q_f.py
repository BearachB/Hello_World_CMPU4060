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
    # The results list is declared as an empty list so that the correct words can be appended to it once they have been found
    results = []

    # The first for loop that iterates through the words list
    for word in words:
        #Variables used to count the occurance of each letter
        i_count = 0
        j_count = 0
        t_count = 0
        x_count = 0

        # The second for loop that iterates through each character in the given word
        for char in word:
            #If a target letter is found, the count for that character is increases by 1
            if "i" in char:
                i_count += 1
            if "j" in char:
                j_count += 1
            if "t" in char:
                t_count += 1
            if "x" in char:
                x_count += 1
        # If the count for all 4 characters is exactly equal to 1 (i.e. each letter appears once)
        if i_count == 1 and j_count == 1 and t_count == 1 and x_count == 1:
            # Add word to results list
            results.append(word)

    # Calculates how long the function took to run, rounded to 2 decimal places
    total_time  = round(time.process_time() - start_time,2)
    # Prints the time taken to run the function
    print("This function took",total_time, "seconds to run.")
    # Prints the number of matching words
    print("There is only", len(results), "word matching this criteria:")
    # Returns the results list
    return results


# Driver code to call the function and print the results
print(puzzle(get_word_list()))
