# Count occurrences of an element in a list
# programme by part.py

def count(lst, x):
    count = 0
    for i in lst:
        if  x == i:
            count = count + 1
    print(count)
count([1,2,5,5,5,6,5,5,5,5,3,4,3,5,3,5], 5)

"""
output:
2
"""