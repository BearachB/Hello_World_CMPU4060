def string_function(input):
    input = input("Enter a string:")

    new_string1 = input[:2]
    new_string2 = input[-2:]

    conc = new_string1+new_string2
    string_length = len(input)

    if string_length < 4:
        print(conc)
        return "This string isn't long enough"
    else:
        print(conc)
        return conc

string_function(input)
