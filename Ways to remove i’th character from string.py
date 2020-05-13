# Programme by parth.py
# Ways to remove i’th character from string
def remove(str,j):
    for i in range(0,len(str)):
        if i != j:
            print(str[i], end="")

a = "APPLE"
b = remove(a, 2)

"""
Output:
APLE
"""