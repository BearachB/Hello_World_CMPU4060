alphabet = "abcdefghijklmnopqrstuvwxyz"

string = 'The quick brown fox jumps over the lazy dog'
string = string.replace(" ", "")
string = string.lower()

set_str = set(string)

len_str = len(string)
len_alph = len(alphabet)
len_set = len(set_str)

if len(set_str) >= len_alph:
    print("This string is a pangram")
