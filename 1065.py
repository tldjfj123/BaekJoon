# 한수 >> 각 자리가 등차수열
import math

num = int(input())

def hansoo(n) :
    res = []
    for i in range(1, n+1) :
        new = str(i)
        if len(new) == 1 :
            res.append(i)
        elif len(new) == 2 :
            res.append(i)
        else :
            std = len(new)
            if std % 2 == 1 :
                for j in range(std-2) :
                    if int(new[j+1]) - int(new[j]) == int(new[j+2]) - int(new[j+1]) :
                        res.append(i)
    return(len(res))

print(hansoo(num))

                

       
        
