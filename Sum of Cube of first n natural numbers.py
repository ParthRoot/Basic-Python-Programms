# Programme by parth.py
# Find the Sum of Cube of first n natural number
def sos():
    sum = 0
    for i in range(1, 6):
        sum = sum + pow(i, 3)
    print(sum)
sos()

"""
output:
225
"""