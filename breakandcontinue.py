# break statment 
for x in range(0,21):
    if x == 11:
        break
    print(x)

#continue statment
for x in range(0,21):
    if x == 11:
        continue
    print(x,end=" ")

num = (1,2,3,4)
name = ("Parth","Lopy","Manvar","Batman")
for x in range(0,len(num)):
    print(f"\n{num[x]} = {name[x]}")


