import time
lst = [1,11,21,31,41,51,61,71,81,91]
for i in lst:
	print( i,end=" "),time.sleep(0.2)
	for j in range(i+1,i+10):
		print(j,end=" "),time.sleep(0.2)
	i = i + 1
	print("\n")

