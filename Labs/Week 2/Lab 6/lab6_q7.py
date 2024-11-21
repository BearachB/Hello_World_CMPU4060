star = ""
tri_size = int(input("Enter how many stars you want on the final line:"))

for i in range(1,tri_size+1):
    star += "*"
    print(star)


#-----------------#

#Other Solution
x = int(input("Please pick a number: "))
for i in range(1, x+1):
    print("*" * i)
