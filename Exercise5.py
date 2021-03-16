# In this , program we input the "num"
# check the number is positive,negative or zero and display 
# print message
# this we use the nested if.....else...! 

num = int(input("Enter the num"))
if num >= 0:
    if num == 0:
        print("this is the zero")
    else:
        print("this is positive")
else:
    print("this is negative")