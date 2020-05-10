# Programme by parth.py
#   Print ASCII value of character
class abc:
    def __init__(self, num):
        self.num = num

    def ASCII(self):
        print(f"ASCII Value of {self.num}:-{ord(self.num)}")


n = input("Enter the CHAR:-")
s1 = abc(n)
s1.ASCII()

"""
Output:
Enter the CHAR:-g
ASCII Value of g:-103
"""


