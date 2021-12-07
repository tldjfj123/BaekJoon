from itertools import combinations

def nandm() :
    n, m = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    
    if m == 1 :
        for a in arr :
            print(a)
    else :
        res = list(combinations(arr, m))
        
        for r in res :
            print(' '.join(list(map(str, r))))

nandm()