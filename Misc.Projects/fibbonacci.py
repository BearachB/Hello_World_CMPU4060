def fibonacci_gen():
    n = int(input("How many digits of the Fibonacci Sequence do you want?: "))
    n1, n2 = 0, 1
    count = 0

    if n <= 0:
        print("Please enter a positive integer!")
    elif n == 1:
        print("Fibonacci Sequence up to", n, ":", n1)
    else:
        print("Fibonacci Sequence")
        while count < n:
            print(n1)
            nth = n1 +n2
            n1 = n2
            n2 = nth
            count +=1

fibonacci_gen()

