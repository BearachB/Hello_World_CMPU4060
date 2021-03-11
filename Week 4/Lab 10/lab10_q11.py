def convert_to_string():
    list = [11, 33, 50]
    string_number = ""
    for el in list:
        string_number += str(el)
    number = int(string_number)
    return(number)

print(convert_to_string())
