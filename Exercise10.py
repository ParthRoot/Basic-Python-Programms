# define function which will take list containing number as input
# return list containing cub of every element
def fun1(a):
    num = []
    for x in a:
        num.append(x**3)
    return num
   
f = int(input("Enter the value of a:-"))
listnumber = list(range(1,f+1))
print(fun1(listnumber))