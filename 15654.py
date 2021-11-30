from itertools import permutations

def nandm() :
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    if m == 1 :
        arr.sort()
        for i in arr :
            print(i)
    else :
        c = sorted(list(permutations(arr, m)))
        
        for i in c :
            print(' '.join(tuple(map(str, i))))

nandm()