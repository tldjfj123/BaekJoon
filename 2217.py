import sys

def rope() :
    n = int(sys.stdin.readline())
    weight = []
    
    for _ in range(n) :
        weight.append(int(sys.stdin.readline()))
    
    weight.sort(reverse = True)
    
    res = []
    
    for i in range(1, n+1) :
        w = weight[i-1] * (i)
        res.append(w)
                
    print(max(res))
    
rope()