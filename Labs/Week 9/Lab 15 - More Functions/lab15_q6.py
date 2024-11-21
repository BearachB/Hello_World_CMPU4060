# Qa
def remove_evens(list1):
    for element in list1:
        if (element % 2) == 0:
            list1.remove(element)
        else:
            pass
    return list1

my_list = [1,2,3,4,5,6,7,8,9,9,21,30,55,40]
print(remove_evens(my_list))

# Qb
def remove_odd(list1):
    for element in list1:
        if (element % 2) != 0:
            list1.remove(element)
        else:
            pass
    return list1

my_list = [1,2,3,4,5,6,7,8,9,9,21,30,55,40]
print(remove_odd(my_list))

# Qc
def remove_bool(list1, bool):
    if bool == True:
        for element in list1:
            if (element % 2) != 0:
                list1.remove(element)
    else:
        for element in list1:
            if (element % 2) == 0:
                list1.remove(element)

    return list1

my_list = [1,2,3,4,5,6,7,8,9,9,21,30,55,40]
my_bool = False
print(remove_bool(my_list,my_bool))
