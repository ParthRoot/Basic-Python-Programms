def fun(z):
	for i in range(1,11):
		print(z,"*",i,"=",i*z,end=" , ")
for z in range(1,10001):
	fun(z)
	print(type(z))
	print("\n")