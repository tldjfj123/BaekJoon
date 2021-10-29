from itertools import combinations

def nm() :
    n, m = map(int, input().split())
    arr = [str(i) for i in range(1, n+1)]
    p = list(map(list, combinations(arr, m)))

    for p in p :
        print(' '.join(p))
    
nm()