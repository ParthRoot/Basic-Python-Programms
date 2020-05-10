# Programme by parth.py
# Find The Area Of Circle
class abc:
    def __init__(self, r):
        self.radius = r

    def area_of_circle(self):
        aof = 0
        pi = 3.14
        aof = pi * pow(self.radius, 2)
        print("Area of Circle:-", aof)

Radius = int(input("Enter the Radius:-"))
s1 = abc(Radius)
s1.area_of_circle()

"""
Output:-
Enter the Radius:-45
Area of Circle:- 6358.0

"""
