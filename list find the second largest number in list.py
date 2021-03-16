# programme by parth.py
# find the second largest number in list
def leargest_number(lst):
    print(f'smallest number is :- {min(lst)}')
    lst.sort()
    print(f'second largest number is :- {lst[-2]}')
leargest_number([1,2,3,5,6])

"""
output:
smallest number is :- 1
second largest number is :- 5
"""