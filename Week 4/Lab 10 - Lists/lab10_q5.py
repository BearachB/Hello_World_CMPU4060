def even_nums(l):
    even_list = []
    for nums in l:
        if nums % 2 == 0:
            even_list.append(nums)
    return even_list
print(even_nums([1,2,3,4,5,6,7,8,9,10]))

