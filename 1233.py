from itertools import permutations
from collections import Counter

def dice() :
    s1, s2, s3 = map(int, input().split())
    
    
    s1 = [i for i in range(1, s1+1)]
    s2 = [i for i in range(1, s2+1)]
    s3 = [i for i in range(1, s3+1)]
    
    res = []
    for i in s1 :
        for j in s2 :
            for k in s3 :
                res.append((i, j, k))
    
    res = Counter(list(map(lambda x : sum(x), res)))
    
    res = [(k, v) for k, v in res.items()]
    
    res.sort(key = lambda x : (-x[1], x[0]))
    
    print(res[0][0])
                
dice()