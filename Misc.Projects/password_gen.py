import random
import time
import string

LETTERS = string.ascii_letters
NUMBERS = string.digits
SPECIALS = string.punctuation

def get_password_length():
        length = input("How long would you like your new password to be? :")
        return int(length)

def password_generator(cbl, length=8):
        printable = fetch_string_constant(cbl)
        printable = f'{LETTERS}{NUMBERS}{SPECIALS}'
        printable = list(printable)
        random.shuffle(printable)
        random_password = random.choices(printable, k=length)
        random_password = ''.join(random_password)

        return random_password
        
def password_combination_choice():
    want_digits = input ("Want digits? (True/False) : ")
    want_letters = input ("Want letters? (True/False) : ")
    want_punctuation = input ("Want special characters? (True/False) :")

    try:
        want_digits = eval(want_digits.title())
        want_letters = eval(want_letters.title())
        want_punctuation = eval (want_punctuation.title())
        return [want_digits, want_letters, want_punctuation]

    except NameError as e:
        print("Invalid answer. Use either 'Y' or 'N'")
        print("Invalidity returns a default, try again or regenerate")

    return [True,True,True]

password_1 = password_generator('cbl', 8)

password_length = get_password_length()
password_2 = password_generator(password_length)

print("Password 1 (" +str(len(password_1)) + " characters" + "): \t\t" + password_1)
print("Password 2 (" +str(len(password_2)) + " characters" + "): \t\t" + password_2)

def fetch_string_constant(choice_list):
        string_constant = ''
        string_constant += NUMBERS if choice_list[0] else ''
        string_constant += LETTERS if choice_list[1] else ''
        string_constant += SPECIALS if choice_list[2] else ''

        return string_constant

if __name__ == '__main__':
        length = get_password_length()
        choice_list = password_combination_choice()
        password = password_generator(choice_list, length)
        print(password)










"""

print(LETTERS)
print(NUMBERS)
print(SPECIALS)



def password_gen():
        
        pass_length = int(input("How many charaters would you like your password to have? : "))
        #pass_comp = int(input("Would you like to use letters & numbers? Y/N :"))

        die_number = random.randint(1,die_sides)
        stop_val = 0
        pos_ans = ['y','Y','Yes','yes','YES','yES','yeS',]
        neg_ans = ['n','N','No','no','NO']
        print("Your shiny new password: ", die_number)
        chance = 1/die_sides
        print("Probability = ", chance)
        time.sleep(1)
        while(stop_val==0):
            mark = str(input("Do you want to re-roll the die? Y/N :"))
            if (mark in pos_ans):
                die_number = random.randint(1,die_sides)
                time.sleep(0.4)
                print(die_number)
            elif (mark == 'n' or mark == 'N' or mark == 'no' or mark == 'No' or mark == 'NO'):
                print ("You have chosen to end the game")
                time.sleep(3)
                print ("pussy")
                stop_val = 1
                break
die_roll()
"""
