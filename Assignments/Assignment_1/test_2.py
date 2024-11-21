def get_word_list():
   """ Return a list of words from a word_list.txt file. """
   data_file = open("word_list.txt", "r")
   word_list = []  # start with an empty word list
   for word in data_file:  # for every word (line) in the file
       # strip off end−of−line characters and make each word lowercase
       # then append the word to the word list
       word_list.append(word.strip().lower())
   return word_list




# def puzzle(word_list):
vowels = set(('a','e','i','o','u','y'))

def count_vowels(word):
    return sum(letter in vowels for letter in word)

my_string = "this is a really weird test"

def get_words(my_string):
    for word in my_string.split():
        if count_vowels(word) == 1:
            print(word)


print(get_words(get_word_list()))
