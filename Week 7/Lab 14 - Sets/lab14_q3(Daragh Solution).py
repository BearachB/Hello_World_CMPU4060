import string
alphabet_str = string.ascii_lowercase
string1 = 'the quick brown fox jumps over the lazy dog'
string1_nospace = "".join(string1.split())

if len(set(string1_nospace)) == len(alphabet_str):
    print("this is a pangram")
else:
    print("this is not a pangram")
