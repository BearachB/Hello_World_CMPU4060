''' Method 1 - much easier
user_int = int(input("Enter an integer: "))
user_bin = bin(user_int).replace("0b","")
print(user_bin)

decimal = 0
for digit in conv_rev:
decimal = decimal*2 + int(digit)
print(decimal)
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

    index = len(conv_rev)
    decimal = 0

    for i in range (0,index):
        power = index - i - 1

        if int(conv_rev[i]) == 1:
            decimal = decimal + 2**power
        else:
            decimal += 0
    print("Your number converted back to decimal is:",decimal)

'''         
        decimal = decrypt_count**2 * int(digit)
        print("Digit:",int(digit))
        decrypt_count += 1


 
        if digit == 0:
            decrypt_count += 0
        else:
            decrypt_count += 2**two_power
            two_power += 1

            print(conv_rev[-1:index:-1])
            index -= 1
    print("Your number converted back to an integer is :",decrypt_count)
'''
