# Programme by parth.py
# Check String is Palindrome or not
def palindrome(s):
    if s == s[::-1]:
        print("Yes it is Palindrome")
    else:
        print("No it is Palindrome")

s = "MALAYALAM"
palindrome(s)

"""
Output:
Yes it is Palindrome
"""
