def get_words():
    data_file = open("movie_list.txt", "r")
    word_dict = {}  # start with an empty word dictionary
    word_list = []  # start with an empty word dictionary
    index_count = 0
    for line in data_file:
        for word in line.strip().split(","):
            # word = word.lower()
            # if word not in word_dict:
            word_list.append(word)
            # word_dict[word] = 0
            # word_dict[word] += 1
        # dict_sorted = sorted(word_dict.items(), key=lambda x:x[1], reverse = True)
    return word_list
print(get_words())

# def create_dict(lst):
#     for word in list:
#         if "(" in word:

