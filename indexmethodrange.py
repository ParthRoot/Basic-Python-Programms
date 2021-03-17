# print list using range function
a=[1,2,3,4,5,6,7,8,9,4,10]
a = list(range(1,11))
print(a)


b = ["hello","world"]
b = list(range(1,5))
print(b)

# pop method can remove last element of list
c = a.pop()
d = a.pop(8)
print(c)
print(a)

# index method
z = [1,2,3,4,5,4,5,7,4,8,9]
print(z.index(5))
print(z.index(4,4,9))

