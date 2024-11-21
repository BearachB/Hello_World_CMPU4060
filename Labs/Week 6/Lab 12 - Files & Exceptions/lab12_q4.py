#Function
def three_nums(a):
    while True:
        try:
            num1 = int(input("Input your first number: "))
            num2 = int(input("Input your second number: "))
            num3 = int(input("Input your third number: "))
            result = (num1 / num2) + num3
            return(result)
            break
        except ValueError:
            print("You have entered an invalid number!")
            print("Try again!")
        except ZeroDivisionError:
            print("You cannot divide by zero!")
            print("Try again!")
print(three_nums(True))
