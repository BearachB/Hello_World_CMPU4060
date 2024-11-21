def get_first_half(user_string):
    str_length = len(user_string)
    if str_length % 2 == 1:
        print("Your string is an odd length")
        return user_string
    else:
        half_point = str_length//2
        half_string = user_string[0:half_point]
        #print(half_string)
        return half_string

print(get_first_half(input("Enter a string: ")))
