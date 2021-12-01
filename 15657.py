from itertools import combinations_with_replacement

def nandm() :
    n, m = map(int, input().split())
    arr = list(input().split())
    arr.sort(key = lambda x : int(x))
    
    if m == 1 :
        for a in arr :
            print(a)
            
    else :
        tmp = list(combinations_with_replacement(arr, m))
        
        for t in tmp :
            print(' '.join(t))
nandm()