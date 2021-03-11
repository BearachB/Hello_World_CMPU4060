my_dict = {'a':15 , 'c':35, 'b':20, 'd':5, 'e':1}

#Qa
count = 0
for key in my_dict:
    count += 1
    print("Key",count, "is", key)

print("\n--------------------\n")

#Qb
value_count = 0
for value in my_dict.values():
    value_count += 1
    print("Value", value_count, "is", value)

print("\n--------------------\n")

#Qc
key_val_count = 0
for key,value in my_dict.items():
    key_val_count += 1
    print("Pair", key_val_count, "is", key,":", value)

print("\n--------------------\n")

#Qd
dict_sort_key = sorted(my_dict.items())
print("Your dictionary sorted by keys looks like:",dict_sort_key)

print("\n--------------------\n")

#Qe
dict_sort_value = sorted(my_dict.items(),key=lambda x:x[1],reverse=True)
print("Your dictionary sorted by values looks like:",dict_sort_value)
