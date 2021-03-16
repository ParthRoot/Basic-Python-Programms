a = "hello"
for x in range(0,len(a)):
    print(a[x])

for x in a:
    print(x)
    
c = input("enter the number")
sum = 0
for x in c:
    sum = sum + int(x)

print(sum)