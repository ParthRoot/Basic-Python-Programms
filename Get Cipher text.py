#Input: 
#arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#k = 3
#Output:  
#[3, 2, 1, 6, 5, 4, 9, 8, 7]

list = [1,2,3,4,5,6,7,8,9]
k = 3
for i in range(k+1):
	c = list[-k+1]
	c.append(list)
print(list)