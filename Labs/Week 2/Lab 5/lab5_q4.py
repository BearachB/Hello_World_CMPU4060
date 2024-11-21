user_num_1 = float(input("Please enter a first number:"))
user_num_2 = float(input("Please enter a second number:"))
user_num_3 = float(input("Please enter a third number:"))

if user_num_1 > user_num_2 and user_num_1 > user_num_3:
    print(user_num_1, "is the largest number you entered")
elif user_num_2 > user_num_3 and user_num_2 > user_num_1:
    print(user_num_2, "is the largest number you entered")
else:
    print(user_num_3, "is the largest number you entered")
