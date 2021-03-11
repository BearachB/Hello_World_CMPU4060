user_weight_lbs = float(input("Input a weight in lbs: "))
user_height_in = float(input("Input a height in inches: "))

user_weight_kg = user_weight_lbs * 0.45359237
user_height_m = user_height_in * 0.0254

user_bmi = user_weight_kg/(user_height_m**2)
print('Your BMI is: ', round(user_bmi,2))
