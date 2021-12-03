from itertools import combinations_with_replacement

def nandm() :
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    if m == 1 :
        arr = list(set(arr))
        arr.sort()
        for a in arr :
            print(a)
    else :
        arr.sort()
        tmp = list(set(list(combinations_with_replacement(arr, m))))
        tmp.sort()
        
        for t in tmp :
            print(' '.join(list(map(str, t))))
            
nandm()