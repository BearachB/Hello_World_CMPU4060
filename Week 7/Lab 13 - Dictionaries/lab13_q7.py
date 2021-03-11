def get_words():
    """ Return a dictionary of word frequencies from a word_list.txt file. """
    data_file = open("hare_and_tortoise.txt", "r")
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

# print(get_words())

def get_freq():
    html_file = open("word_cloud.html", "r")
    html_lines = html_file.readlines()
    # print(html_lines[8])
    for key in get_words():
        for element in key:
            # get_words()[key][1] *= 10
            print(element)
            print("-----")

print(get_freq())
