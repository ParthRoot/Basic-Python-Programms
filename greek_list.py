# Python program to demonstrate  
# Creation of List
def abs():
	for i in range(30):
		print("_",end=" ")
	print("\n")
	
# Creating a List
List = []
print("Creating a List")
print(List)
abs()

# Creating a List of numbers
print("Creating a list of numbers")
List = [1,2,3,4,5]
print(List)
abs()

# Creating a List of strings and accessing 
# using index 
print("Creating a List of strings and accessing ")
List = ["Apple","Banana","Graps","Watermelon","Orange"]
print(List[3])
abs()

# Creating a Multi-Dimensional List 
# (By Nesting a list inside a List)
print("Creating a Multi-Dimensional List") 
List = [["Apple","Orange","Banana"],[1,2,3,4,5]]
print(List)
abs() 

# Creating a List with  
# the use of Numbers 
# (Having duplicate values) 
print("Creating a List Having duplicate values")
List = [1,1,1,1,2,3,"a","b","a","s"]
print(List)
abs()

#length of list
print("Length of list:-",len(List))
abs()

#Adding a element to a list
#Append method
list = []
print("This is the blank list")
print(list)
abs()

print("Adding element in list")
list.append(555)
print(list)
abs()

#Adding element using the for loop
print("Adding Element using the forloop")
for i in range(11):
	list.append(i)
print(list)
abs()

#Adding tuple to the list
print("Adding tuple to the list")
tup = ("a","b","c","d")
list.append(tup)
print(list)
abs()

#Adding List in List
print("Adding list to list")
list.append(List)
print(list)
abs()

#Insert Element sepecific Position in list
#Insert Method
print("Inser Element in Specific Position to List")
lst = [2,3,4,5,5]
lst.insert(1,"Parth")
print(lst)
abs()

#Insert a multiple element in list 
#extend Method
print("Insert Multiple element in list")
lst.extend(["Parth","Lopy","Bapu","Sonu"])
print(lst)
abs()

#accessing a element from list
print("Accessing element in list")
l = [["1","4","3"],["Apple","Orange","Mango"]]
print(l[0][1])
abs()
#Use the Negative Indexing
print("Using the negative Indexing")
print(lst[-1])
abs()

#Remove element in list
#remove Method
a = []
for i in range(1,21):
	a.append(i)
print(a)

a.remove(5)
print(a)
abs()
print("remove the multiple element")
for x in range(6, 10):
	a.remove(x)
print(a)
abs()

#delete element 
#pop method
print("Using POP method")
a.pop()
print(a)


