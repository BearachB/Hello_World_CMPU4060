def o_words(list):
    count = 0
    for words in list:
        if words[0] == "o" or words[0] == "O":
            count += 1
    return count

print(o_words(['Always', 'look', 'on', 'the', 'bright', 'side', 'of', 'life']))
