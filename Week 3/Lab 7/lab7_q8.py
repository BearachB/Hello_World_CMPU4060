
text = input("Enter a string to apply a Caesarian Shift to it: ")
shift = int(input("How many characters do you want to shift? "))
out = ""

for i in text:
    encrypted_string = ord(i)+shift
    shifted_string = chr(encrypted_string)
    out += shifted_string

print(out)

