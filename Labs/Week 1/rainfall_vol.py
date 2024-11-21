
#Prompt user to input cm of rainfall
cm_str = input("Input the amount of rainfall in cm: ")
cm_int = int(cm_str)

#Convert acre to sq m. Conversion factor = 4046.86
volume = cm_int*0.01*4046.86

litres = volume*1000

print(cm_int, 'will yield', litres, 'litres of rain')
