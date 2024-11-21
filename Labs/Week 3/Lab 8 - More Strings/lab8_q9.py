print("To exit, enter a full stop ('.') when prompted")
count = 1
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxz"
ay = "ay"
yay = "yay"
while count == 1:
    user_input = input("Input a string: ")
    first_letter = user_input[0]
    second_letter = user_input[1]
    if first_letter in vowels:
        print(first_letter, "is a vowel")
        pig_output = user_input+yay
        print(pig_output)
    elif user_input == ".":
        count = 0
    else:
        print(first_letter, "is a consonant")
        if second_letter in consonants:
            input_length = len(user_input)
            remove_letter = user_input[2:input_length]
            pig_output = remove_letter+first_letter+second_letter+ay
            print("2 consonants")
            print(pig_output)
        else:
            input_length = len(user_input)
            remove_letter = user_input[1:input_length]
            pig_output = remove_letter+first_letter+ay
            print("1 consonant")
            print(pig_output)


