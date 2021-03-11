def caesar_cipher():
    text = input("Enter a string to apply a Caesarian Shift to it: ")
    shift = int(input("How many characters do you want to shift? "))
    out = ""
    for i in text:
        encrypted_string = ord(i)+shift
        shifted_string = chr(encrypted_string)
        out += shifted_string
    return(out)

def caesar_brutus():
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message = input("Copy your cipher in here:")

    for key in range(len(LETTERS)):
        translated = ''
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                    translated = translated + LETTERS[num]
                else:
                    translated = translated + symbol
        print('Hacking key #%s: %s' % (key, translated))

# def caesar_cipher_brute_force(out):
#     letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
#     for key in range(len(letters)):
#         decrypt = ''
#         for symbol in out:
#             if symbol in letters:
#                 num = num - key
#                 if num < 0:
#                     num = num + len(letters)
#                 decrypt = decrypt + letters[num]
#             else:
#                 decrypt = decrypt + symbol
#     return('Hacking key #%s: %s',key, decrypt)


# message = 'GIEWIVrGMTLIVrHIQS' #encrypted message
# LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
# for key in range(len(LETTERS)):
#    translated = ''
#    for symbol in message:
#       if symbol in LETTERS:
#          num = LETTERS.find(symbol)
#          num = num - key
#          if num < 0:
#             num = num + len(LETTERS)
#          translated = translated + LETTERS[num]
#       else:
#          translated = translated + symbol
# print('Hacking key #%s: %s' % (key, translated))
# print(caesar_cipher())
print(caesar_brutus())
