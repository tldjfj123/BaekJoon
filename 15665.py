from itertools import product

def nandm() :
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    if m == 1 :
        arr = sorted(list(set(arr)))
        for i in range(len(arr)) :
            print(arr[i])
    
    else :
        res = list(product(arr, repeat = m))
        res = sorted(list(set(res)))
        
        for r in res :
            print(' '.join(map(str, r)))
            
nandm()