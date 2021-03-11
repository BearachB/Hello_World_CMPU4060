def calc_factorial(x):
    x = int(input("Enter an integer to calculate its factorial: "))
    count = 1
    for i in range(1,x+1):
        count *= i
        #print(i, "*", i-1, "=",count)
    final_fact = count
    print("The factorial of",x,"is:",final_fact)

calc_factorial(20)
