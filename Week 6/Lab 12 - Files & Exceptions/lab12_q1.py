number_str = input("Input a floating-point number: ")
while True:
    try:
        number_float = float(number_str)
    except ValueError:
        print("That is not a valid float")
        number_str = input("Input a floating-point number: ")
    else:
        print(number_float)
        break

print("Number is",number_float)
