string1 =  'the big dwarf only jumps'
string2 =  'given string is Heterogram'

string1 = string1.replace(" ","")
string2 = string2.replace(" ","")


len1 = len(string1)
len2 = len(string2)

set1 = set(string1)
set2 = set(string2)

set_len1 = len(set1)
set_len2 = len(set2)

if len1 == set_len1:
    print("String 1 is a heterogram")
else:
    print("String 1 is not a heterogram")

if len2 == set_len2:
    print("String 2 is a heterogram")
else:
    print("String 2 is not a heterogram")



def heterogram(input):
    alphabets = [ch for ch in input if ord('a') <= ord(ch) <= ord('z')]

    if len(set(alphabets)) == len(alphabets):
        print("Yes, it is a heterogram")
    else:
        print("No")

print(heterogram("Given string is heterogram"))
