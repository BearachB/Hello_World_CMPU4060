final_number = int(input("Enter an integer: "))
number = 1

while number <= final_number:
    count = 1
    sum = 0

    while count <= number:
        sum += count
        count += 1

    if sum % (count - 1) == 0:
        print("The sum is: ",sum)
    number += 1
