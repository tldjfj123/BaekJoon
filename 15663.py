from itertools import permutations

def nandm() :
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    if m == 1 :
        arr = sorted(list(set(arr)))
        for a in arr :
            print(a)
    
    else :
        res = list(set(permutations(arr, m)))
        res.sort()
        for r in res :
            print(' '.join(list(map(str, r))))
    
nandm()