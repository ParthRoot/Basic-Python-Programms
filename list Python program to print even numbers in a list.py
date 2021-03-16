# Programme by parth.py
# Python program to print even numbers in a list

def even(lst):
    for i in lst:
        if i % 2 == 0:
            print(i, end=" ")
def odd(lst):
    for i in lst:
        if i % 2 != 0:
            print(i, end=" ")
print("Even Number is-:")
even([1,2,3,4,5,6,7,8,9])
print("\nodd Number is:-")
odd([1,2,3,4,5,6,7,8,9])

"""
output:
Even Number is-:
2 4 6 8 
odd Number is:-
1 3 5 7 9 
"""

