def my_function(x):
    for i in range(0,user_input+1):
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")

user_input = int(input("Enter a number: "))
my_function(user_input)
