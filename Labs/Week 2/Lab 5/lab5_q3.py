user_num_1 = int(input("Please enter a first number:"))
user_operation = input("What operation would you like to do? (+,-,*,/):")
user_num_2 = int(input("Please enter a second number:"))

if user_operation == "+":
    print("The result of your calculation is:",user_num_1 + user_num_2)
elif  user_operation == "-":
    print("The result of your calculation is:",user_num_1 - user_num_2)
elif  user_operation == "*":
    print("The result of your calculation is:",user_num_1 * user_num_2)
elif  user_operation == "/":
    print("The result of your calculation is:",user_num_1 - user_num_2)
