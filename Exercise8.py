import random
win = random.randint(1,10)
while True:
    num = int(input("enter the num :-"))

    if num == win:
        print("you enter the right number")
        break
    else:
        if num > win:
            print('number is heigh')
        else:
            print("number is low")
        continue