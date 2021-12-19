from itertools import combinations

def nandm() :
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    if m == 1 :
        arr = sorted(list(set(arr)))
        for a in arr :
            print(a)
    else :
        res = list(combinations(arr, m))
        res = sorted(list(set(res)))
        
        for r in res :
            print(' '.join(map(str, r))) 

nandm()