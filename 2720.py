import sys

def dongar97() :
    n = int(sys.stdin.readline())
    coin = [25, 10, 5, 1]
    for _ in range(n) :
        res = []
        money = int(sys.stdin.readline())
        
        for c in coin :
            if money // c > 0 :
                res.append(str(money // c))
                money %= c
            else :
                res.append(str(0))
        print(' '.join(res))            
        
dongar97()