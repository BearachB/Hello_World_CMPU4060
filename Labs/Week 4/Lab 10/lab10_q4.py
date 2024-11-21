def a_words(list, char):

    char = input("Input the character you want to check for: ")
    count = 0
    for words in list:
        if words[0] == char:
            count += 1
    return count

print(a_words(['Always', 'look', 'on', 'the', 'bright', 'side', 'of', 'life'], 'a'))
