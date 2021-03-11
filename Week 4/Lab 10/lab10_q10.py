def l_diff(list1, list2):
    list_difference = []
    for el in list1:
        if el not in list2:
            list_difference.append(el)
    return list_difference

test_list1 = [1, 2, 3, 4, 5, 6]
test_list2 = [10, 9, 8, 7, 6]

print(l_diff(test_list2, test_list1))
