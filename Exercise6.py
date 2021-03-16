# ask user for natural number (a)
# print sum from 1 to a

a = int(input("Enter a:"))
sum = 0
i = 1
while i <= a:
    sum = sum + i
    i = i + 1
print(sum)