# Easy way using in built Max function
# def return_max(list):
#     return max(list)
# print(return_max([1,2,3,4,5,6]))

def return_max(list):
    largest = list[0]
    for elements in list:
        if elements > largest:
            largest = elements
    return largest
print(return_max([1,2,3,4,5,6]))
