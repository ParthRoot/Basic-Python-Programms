# Programme by parth.py
# Print all positive or negative number in list
print("Positive Number:-")
def positive():
    for i in range(-4, 10):
        if i >= 0:
            print(i,end=" ")
positive()

print("\nNegative Number")
def negative():
    for i in range(-4, 10):
        if i < 0:
            print(i,end=" ")
negative()

"""
Output:
Positive Number:-
0 1 2 3 4 5 6 7 8 9 
Negative Number
-4 -3 -2 -1 
"""