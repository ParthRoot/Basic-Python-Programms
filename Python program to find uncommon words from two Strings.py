# Programme by parth.py
# Python program to find uncommon words from two Strings

def uncomman(s1, s2):

    l1 = s1.split(" ")
    l2 = s2.split(" ")
    for i in l1:
        if i not in l2:
            print(i,end=" ")
    for j in l2:
        if j not in l1:
            print(j)

uncomman("Parth Patel","Jaimin Patel")

