from itertools import permutations

def all() :
    n = int(input())
    arr = [i for i in range(1, n+1)]
    
    res = list(permutations(arr, n))
    
    for r in res :
        print(' '.join(list(map(str, r))))
       
all()