user_input = int(input("Enter a number:"))

def my_function(x):
    count = 0
    for i in range(1,user_input+1):
        print(i)
        count += i
    print("the sum of all numbers shown is",count)
    return count
my_function(user_input)
