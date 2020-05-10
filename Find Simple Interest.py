class abc:
    def __init__(self,p,r,n):
        self.p = p
        self.r = r
        self.n = n

    def simple_interest(self):
        Interest = 0
        Interest = (self.p * self.r * self.n)/100
        print("Interest:-",Interest)

s1 = abc(10,10,10)
s1.simple_interest()



