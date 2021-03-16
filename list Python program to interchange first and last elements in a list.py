# Programme by parth.py
# Python program to interchange first and last elements in a list
def swapping(lst):
    a = len(lst)

    # swapping
    temp = lst[0]
    lst[0] = lst[a-1]
    lst[a-1] = temp

    print(lst)
lst = [1,2,3,4,5,6]
swapping(lst)


