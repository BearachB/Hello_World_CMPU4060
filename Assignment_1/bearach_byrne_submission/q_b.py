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
    # The pronouns we are looking for
    pronouns = ['thou', 'thee', 'thine', 'thy', 'i', 'me', 'mine', 'my', 'we', 'us', 'ours', 'our', 'you', 'yours',
                'your', 'he', 'him', 'his', 'she', 'her', 'hers', 'it', 'its', 'they', 'them', 'theirs', 'their']
    # The matching words will be appended to this list once they have been found
    results = []
    # The combinations of any 2 pronouns will be stored here
    combinations = []

    # These 2 for loops iterate through the pronoun list to create all combinations of 2 pronouns
    for index in range(0, len(pronouns)):
        for otherindex in range(0, len(pronouns)):
            # Creates new_word by appending 2 pronouns
            new_word = pronouns[index] + pronouns[otherindex]
            # Appends the pronoun combinations to the list
            combinations.append(new_word)

    # Iterates through the word list
    for word in words:
        # Iterates through the list of pronoun combinations
        for combo in combinations:
            # If the pronoun combination is the same as the word
            if (combo == word):
                # Add the word to the results list
                results.append(word)

    #Prints the amount of combinations and all combinations, this was mainly for troubleshooting when writing the code.
    print("There are",len(combinations), "combinations:")
    print(combinations,"\n")
    # Calculates how long the function took to run, rounded to 2 decimal places.
    total_time  = round(time.process_time() - start_time,2)
    # Prints the time taken to run the function
    print("This function took",total_time, "seconds to run.")
    # Prints a statement saying how many words match the criteria
    print("There are", len(results), "words matching this criteria:")
    # Returns the results list
    return results


# Driver code to call the function and print the results
print(puzzle(get_word_list()))
