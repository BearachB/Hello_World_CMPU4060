#My Solution
# def common_mems(l1, l2):
#     result = False
#     for x in l1:
#         for y in l2:
#             if x == y:
#                 result = True
#                 return result
#     return result
#
# test_list1 = [10, 2, 3, 4]
# test_list2 = [10, 9, 8, 7, 6]
#
# print(common_mems(test_list1, test_list2))


#Lucas' solution:
def common_member(list1, list2):
    for el1 in list1:
        if el1 in list2:
            return True
    return False

list1 = [1,2,3,4,5]
list2 = [10,9,8,7,6,5]

print(common_member(list1,list2))
