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
    # The vowels we are looking for
    vowel = ["a","e","i","o","u"]
    # The matching words will be appended to this list
    results = []

    # The first for loop that iterates through the list of 45,000 words
    for word in words:
        # If the word is 7 characters long
        if len(word) == 7:
            # Sets vowel_control equal to the number of vowels in the word
            vowel_control = sum(True for letter in word if letter in vowel)
            # If vowel control is exactly equal to 1
            if vowel_control == 1:
                # If s is not present in word
                if 's' not in word:
                    # Add word to the results list
                    results.append(word)

    # Calculates how long the function took to run, rounded to 2 decimal places
    total_time  = round(time.process_time() - start_time,2)
    # Prints the time taken to run the function
    print("This function took",total_time, "seconds to run.")
    # Prints a statement saying how many words match the criteria
    print("There are ", len(results), "words matching this criteria")
    # Returns the results list
    return results


# Driver code to call the function and print the results
print(puzzle(get_word_list()))
