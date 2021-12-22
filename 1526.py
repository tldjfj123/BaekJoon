from itertools import product

def biggest() :
    n = int(input())
    silver = [4, 7]
    
    sub = []
    
    for i in range(1, len(str(n))+1) :
        p = list(product(silver, repeat = i))
        for p in p :
            sub.append(p)
    
    sub = list(map(lambda x : int(''.join(list(map(str, x)))), sub))
    
    res = 0
    for s in sub :
        if s > n :
            break
        res = s
        
    print(res)
    
biggest()