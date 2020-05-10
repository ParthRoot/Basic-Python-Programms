# Programme by parth.py
# Print Fibonacci Number
def fib(n):
    a = 0
    b = 1

    for i in range(2, n + 1):
        c = a + b
        print(c,end=" ")
        a = b
        b = c
fib(10)

"""
Output:- 
1 2 3 5 8 13 21 34 55

"""