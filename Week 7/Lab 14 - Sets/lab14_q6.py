def get_words():
    """ Return a dictionary of word frequencies from a word_list.txt file. """
    data_file = open("movie_list.txt, "r")
    word_dict = {}  # start with an empty word dictionary
    for line in data_file:
        for word in line.strip().split():
            word = word.lower()
            l = len(word)
            if word not in word_dict:
                word_dict[word] = 0
            word_dict[word] += 1
        dict_sorted = sorted(word_dict.items(), key=lambda x:x[1], reverse = True)
    return dict_sorted
