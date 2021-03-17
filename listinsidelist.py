list1=[[1,2,3],[4,5,6],[7,8,9]]
print(list1)
for sublist in list1:
    for j in sublist:
        print(j)


list2 = [["a","b","c"],["d","e","f"],["g","h","i"]]
print(list2)
for sublist in list2:
    for x in sublist:
        print(x,end="\t")