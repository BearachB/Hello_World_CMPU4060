user_weight = float(input("Input a weight in kg: "))
user_height_cm = float(input("Input a height in cm: "))

user_height_m = user_height_cm/100

user_bmi = user_weight/(user_height_m**2)


print('Your BMI is: ', round(user_bmi, 2))
if user_bmi < 18.4:
    bmi_diff = 18.4 + user_bmi
    print("You are classified as Underweight")
    print("You should try to raise your BMI by", round(bmi_diff,2), "to be classified as Normal Weight")
elif 18.4 < user_bmi < 25:
    print("You are classified as Normal Weight")
elif 25 < user_bmi < 29.9:
    print("You are classified as Obese Class I")
elif 29.9 < user_bmi < 34.9:
    print("You are classified as Obese Class II")
elif user_bmi > 39.9:
    print("You are classified as Obese Class III")

print("\nFor for information on BMI, please visit: https://www.euro.who.int/en/health-topics/disease-prevention/nutrition/a-healthy-lifestyle/body-mass-index-bmi")
