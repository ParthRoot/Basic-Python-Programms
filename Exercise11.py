# define function which will  take list as a argument and this function
# which return the reverse list

# reverce method
def fun1(list1):
    list1.reverse()
    return list1
a = [1,2,3,4,5,6,7,8,9]
print(fun1(a))

# string slicing
def fun2(list1):
    return list1[::-1]

print(fun2(a))

# also try this  with pop and append method
def append_pop(z):
    r = []
    for x in range(len(z)):
        y = z.pop()
        r.append(y)
    return r

f = ["apple","orange","banana"]
print(append_pop(f))