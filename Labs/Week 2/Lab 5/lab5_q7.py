
list_of_ints = []

for number in range(100,1000):
    if number % 17 == 0:
        list_of_ints.append(number)

print("The three digit numbers that are divisible by 17 are:",list_of_ints)
