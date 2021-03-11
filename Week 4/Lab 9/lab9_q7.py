user_input = ""
def remove_odd_chars(user_input):
    new_string = user_input[0::2]
    print(new_string)
    return new_string

remove_odd_chars(input("What args do you want to pass?: "))
