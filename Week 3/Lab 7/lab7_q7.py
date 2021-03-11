
text = input("Enter a string: ")
a = ""
for i in range(1, len(text) + 1):
    a += text[len(text) - i]

print(a)
