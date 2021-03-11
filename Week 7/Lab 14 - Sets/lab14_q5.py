#Q5a
print("----- Question A -----")
def q5a(first,last):
    usr_first = first
    usr_last = last

    usr_first_list = list(usr_first)
    usr_last_list = list(usr_last)

    common_letters = []

    for letter in usr_first_list:
        if letter in usr_last_list:
            common_letters.append(letter)

    return common_letters


usr_first = input("Enter your first name: ")
usr_last = input("Enter your last name: ")
print(q5a(usr_first,usr_last))


#Q5b
print("----- Question B -----")
def q5b(first,last):
    usr_first = first
    usr_last = last

    usr_first_set = set(usr_first)
    usr_last_set = set(usr_last)

    common_letters = usr_first_set.intersection(usr_last_set)

    return common_letters


usr_first = input("Enter your first name: ")
usr_last = input("Enter your last name: ")
print(q5b(usr_first,usr_last))


#Q5c
print("----- Question C -----")
def q5c(first,last):
    usr_first = first
    usr_last = last

    usr_first_set = set(usr_first)
    usr_last_set = set(usr_last)

    common_letters = usr_first_set.symmetric_difference(usr_last_set)

    return common_letters


usr_first = input("Enter your first name: ")
usr_last = input("Enter your last name: ")
print(q5c(usr_first,usr_last))




