class abc:
    def __init__(self, p, r, t):
        self.p = p
        self.r = r
        self.t = t

    def compound_interest(self):
        Interest = 0
        Interest = self.p * (pow((1 + self.r / 100), self.t))
        print(f"Compound Interest:-{Interest}")


s1 = abc(1200, 5.4, 2)
s1.compound_interest()
