cigars_no = int(input("Input the number of cigars available: "))
weekend = bool(input("Is it this weekend? True or False: "))
successful_party = bool

if 40 < cigars_no > 60 and weekend == False:
    successful_party = True
    print("This will be a successful party")
elif 40 < cigars_no and weekend == True:
    successful_party = True
    print("This will be a successful party")
else:
    successful_party = False
    print("This will not be a successful party")
