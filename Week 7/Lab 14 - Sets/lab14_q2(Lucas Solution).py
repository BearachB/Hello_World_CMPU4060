def heterogram(input):
    alphabets = [ch for ch in input if ord('a') <= ord(ch) <= ord('z')]

    if len(set(alphabets)) == len(alphabets):
        return ("Yes, it is a heterogram")
    else:
        return("No, not a heterogram")

print(heterogram("Given string is heterogram"))
