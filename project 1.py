import random
import math as m
while True:
    a = int(input("range start: "))
    b = int(input("range finish: "))
    ran = random.randrange(a, b)
    print(ran)
    if ran%2==0:
        print(ran,"is even number")
    else:
        print(ran,"is odd number")
    if ran>0:
        print(ran,"positive number")
    else:
        print(ran,"negative number")
    flag=0
    if (ran > 1):
        for k in range(2, int(m.sqrt(ran)) + 1):
            if (ran % k == 0):
                flag = 1
            break
        if (flag == 0):
            print(ran, "is a Prime Number!")
        else:
            print(ran, "is Not a Prime Number!")
    else:
        print(ran, "is Not a Prime Number!")

