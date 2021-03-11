# # #Q7a
# squareList = [n**2 for n in range(1,101)]
# print(squareList)
#
# #Q7b
# colors = ['Red', 'Blue', 'Green', 'Black', 'White']
# newList = [x.upper() for x in colors]
# print(newList)
#
# #Q7c
# numberList = [n for n in range(1,1001) if n%7 == 0]
# print(numberList)

# #Q7d
# myStr = "Hello world there are 8 spaces in this word"
# spaceCount = [i for i in myStr if i.count(" ")]
# print(spaceCount)
# print("There are", len(spaceCount), "spaces in your string.")

# #Q7e
# myStr = "This will remove all vowels in the string."
# vowels = ["a","e","i","o","u"]
# vowelRemove = [letter for letter in myStr if letter.lower() not in vowels]
# print("".join(vowelRemove))

# #Q7f
# myStr = "Hello this will remove all words that are less than 4 letters"
# newList = [word for word in myStr.split() if len(word) < 4]
# print("".join(newList))


#Q7g
part_g = [number for number in range(1, 1001) if True in [True for i in range(2,10) if number % i == 0]]
print(len(part_g))
