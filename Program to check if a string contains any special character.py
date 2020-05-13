# Programme by parth.py
# Program to check if a string contains any special character

sc = ['!', '@', '$', '#', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '<', '>']
str = "patel"
for i in str:
    if i in sc:
        print("String is Not Accepted")
        break
else:
    print("String Is Accepted")

"""
Output:
String is Not Accepted
"""