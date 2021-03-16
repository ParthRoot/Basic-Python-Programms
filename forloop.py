x = 0

for x in range(4):
    for y in range(4):
        print("*",end=" ")
        y = y + 1
    x = x + 1
    print()


sum = 0
for x in range(1,11):
    sum = sum + x
    x = x + 1
print(sum)

# calculate sum of digit
num = input("enter the number-:")
sum = 0
for x in range (0,len(num)):
    sum = sum + int(num[x])
    x = x + 1
print(sum)    






