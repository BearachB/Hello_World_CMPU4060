
number_str = int(input("Please enter a number to check:"))

divisor = 1
sum_of_divisors = 0
while divisor < number_str:
    if number_str % divisor == 0:
        sum_of_divisors = sum_of_divisors + divisor
    divisor += 1

if number_str==sum_of_divisors:
    print(number, "is perfect")
    elif
