def fact(n):
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i
    print(f"Factorial of {n} = {factorial}")

n=int(input("Enter the Value of n:-"))
fact(n)
