def part_of_string(str, index_1, index_2):
    new_str = str[:index_1] + str[index_2+1:]
    return new_str
print(part_of_string("Hello World", 1, 9))
