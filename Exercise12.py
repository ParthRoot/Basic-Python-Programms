# create a function that take  list of word as argument and return  list with reverse 
# of every element  in that list
b = ["apple","orange","banana","cherry"]
def funz(a):
    c = []
    for i in a:
        c.append(i[::-1])
    return c

print(funz(b))


    