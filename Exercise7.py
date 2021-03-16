# ask user to input number containing more than 4 digit
# example 1234
num = input("Enter the num:")
# sum = 1+2+3+4
print(len(num))
 
i = 0
sum = 0
while i < len(num):
    sum = sum + int(num[i])
    i = i + 1
print(sum)

