import math

def squared() :
    m = int(input())
    n = int(input())
    
    m_ = math.floor(math.sqrt(m))
    n_ = math.ceil(math.sqrt(n))
    
    res = []
    for i in range(m_, n_+1) :
        if i ** 2 in range(m, n+1) :
            res.append(i**2)
    
    if len(res) == 0 :
        print(-1)
    else :
        print(sum(res))
        print(min(res))
    
squared()