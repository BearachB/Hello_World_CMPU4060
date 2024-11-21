def remove_dups(l):
    new_list = []
    for i in l:
        if i not in new_list:
            new_list.append(i)
    return new_list

test_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
print(remove_dups(test_list))
