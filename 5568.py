from itertools import permutations

def card() :
    n = int(input())
    k = int(input())
    arr = [input() for _ in range(n)]
    
    res = []
    
    for f in list(map(list, permutations(arr, k))) :
        t = int(''.join(f))
        if t not in res :
            res.append(t)
            
    print(len(res))
card()