import random

string = input("Please enter a string to swap two random letters:")
string_length = len(string)

rand_int1 = random.randint(0,string_length-1)
rand_int2 = random.randint(0,string_length-1)
#print(string_length)

if rand_int1 == rand_int2:
    rand_int2 = random.randint(0,string_length)

#print(rand_int1)
#print(rand_int2)

rand_char1 = string[rand_int1]
rand_char2 = string[rand_int2]

print("Random letter 1:",rand_char1)
print("Random letter 2:",rand_char2)

if rand_int1 < rand_int2:
    print(string[0:rand_int1] + string[rand_int2] + string[rand_int1 + 1:rand_int2] + string[rand_int1] + string[rand_int2 +1:]) #go from 0 to rand_int1,insert rand_int2, rand_int1 to rand_int2, insert rand_int1, rand 2 until end
elif rand_int2 < rand_int1:
    print(string[0:rand_int2] + string[rand_int1] + string[rand_int2 + 1:rand_int1] + string[rand_int2] + string[rand_int1 +1:])
else:
    print(string)

