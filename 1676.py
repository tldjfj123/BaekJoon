import math

def zero() :
    num = int(input())
    res = list(str(math.factorial(num)))
    count = 0
    for i in range(len(res)-1, -1, -1) :
        if res[i] == '0' :
            count += 1
        else :
            break
    print(count)       

zero()