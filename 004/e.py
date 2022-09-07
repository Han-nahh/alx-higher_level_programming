li=[]
repeat=0
try:
    for i in range (0,101):
        vote=int(input("Enter vote in num or press any char to exit:"))# cook your dish here
        li.append(vote)
except:
    print(" ")
finally:
    print(li)
    dup=set(li)
    print(dup)
    y=len(li)
    z=len(dup)
    x=y-z
    print("The values of fraud = ")
    print(x)


