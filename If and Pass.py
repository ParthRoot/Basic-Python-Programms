a = 18
if a > 17:
    print("Yoy will get driving license")

# after if statment we can not writing anything this situation we use the "pass" statment
if a > 17:
    pass

print("hello world")

# else statment

if a > 17:
    print("You apply for driving license")
else: 
    print("You can not apply for driving license")

# nested if else statment
winning_number = 2

if winning_number == 5:
    print("User enter the valid number")
else:
    if winning_number > 5:
        print("this is hight number")
    else:
        print("this is low number")  

# if-elif-else 
Age =  int(input("Enter the age:-"))
if Age <= 12:
    print("No tickets")
elif Age > 12 and Age <= 25:
    print("tickets=Rs 50")
elif Age > 25:
    print("tickers=Rs 100")
else:
    print("valid age")




