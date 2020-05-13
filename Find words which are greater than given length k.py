# Programme by parth.py
# Find words which are greater than given length k
def string_k(str, k ):
    a = []
    str =  str.split(" ")
    for x in str:
        if len(x) > k:
            a.append(x)
    print(a)

string_k("parth patel poc", 4)

"""
Output:
['parth', 'patel']
"""
