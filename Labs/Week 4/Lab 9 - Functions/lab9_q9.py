def insert_middle(str, word):
    if len(str) %
    string_length = len(str)
    str_mid = string_length//2
    return str[:str_mid] + word + str[str_mid:]

print(insert_middle("{{}}","PHP"))
