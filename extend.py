list = [1,2,3]
print(list)

list.extend(["hello","parth","patel"])
print(list)

list1 = ["you","are","mozila"]
list.append(list1)
print(list)

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
print(list[0])

list2=[[1,2,3],[4,5,6]]
print(list2[0][2])

# negative indexx

print(list1[-5])

# remove the element
list1.remove(4)
print(list1)

for i in range(5,9):
	list1.remove(i)
print(list1)

#pop
list1.pop(9)
print(list1)

#copy
list2 = list1.copy()
print(list2)


