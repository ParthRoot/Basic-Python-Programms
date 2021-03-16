# Ask user to enter the full name
name = input("Enter the full name-:  ")

print(f"Full name:-{name} \t" +name.lower()+"\t" +name.upper() )
print(name.count("a"))

# take two comma seperate input for user

UserName,a=input("Enter the user name and password:- ").split()
print(f"user name is-: {UserName} \n a is - :{a} {name.count(a.strip().lower())}")







