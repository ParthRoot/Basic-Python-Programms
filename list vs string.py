# string imputable we can not change original string
# we can create a new variable and store the new string but we can not change the original string

str1="hello"
print(str1.title()) 
print(str1) # not change the original string

# list are mutable we change the list
a = [1,2,3,4]
print(a)
a.remove(3)
print(a) # we can change the list