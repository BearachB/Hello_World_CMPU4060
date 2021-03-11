def sum_neighors(listA):
    new_list = []

    if len(listA) == 0:
        return new_list

    if len(listA) == 1:
        new.list.append(listA[0])
        return new_list

    new_list.append((listA[0] + listA[1]))

    for i in range(1,len(listA) - 1):
        new_list.append(listA[i - 1] + listA[i] + listA[i + 1])

    new_list.append(listA[-1])
