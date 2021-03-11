def hundred_ints():
    list_ints = []
    length = int(input("What index number do you want?: "))
    for i in range(100):
        list_ints.append(length)
    return list_ints

print(hundred_ints())
