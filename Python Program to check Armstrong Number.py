class abc:
    def __init__(self,num):
        self.num = num

    def arms(self):
        num1 = 0
        for i in str(self.num):
            num1 = num1 + pow(int(i),3)
        if num1 == self.num:
            print(f"yes,{self.num} is Armstrong number")
        else:
            print(f"No,{self.num} is not Armstrong number")
num = int(input("Enter the Num:-"))
s1 = abc(num)
s1.arms()

