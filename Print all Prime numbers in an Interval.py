# Programme by parth.py
# Print all Prime Numbers in an Interval
class abc:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def prime_num(self):
        for i in range(self.start, self.end):
            if i > 1:
                if i == 2 or i == 3 or i == 5:
                    print(i, end=" ")
                elif i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
                    pass
                else:
                    print(i, end=" ")
            else:
                pass

s1 = abc(1, 50)
s1.prime_num()

"""
Output:-
2 3 5 7 11 13 19 23 29 31 37 41 43 47 49
"""
