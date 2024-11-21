''' Method 1 - much easier
user_int = int(input("Enter an integer: "))
user_bin = bin(user_int).replace("0b","")
print(user_bin)
'''

user_int = int(input("Enter an integer: "))
conv=''

if user_int == 0:
    print("0")

elif user_int < 0:
    print("That is beyond the scope of this program")

else:
    while user_int > 0:
        if user_int%2 ==0:
            conv += '0'
        else:
            conv += '1'
        user_int = user_int//2
        conv_rev = conv[::-1]
    print("Your number in binary is:",conv_rev)

