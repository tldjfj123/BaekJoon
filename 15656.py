from itertools import product

def nandm() :
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    
    if m == 1 :
        for a in arr :
            print(a)
    else :
        res = list(product(arr, repeat = m))
        for r in res :
            print(' '.join(list(map(str, r))))
            
nandm()