from itertools import permutations

def nandm() :
    n, m = map(int, input().split())
    arr = [str(i) for i in range(1, n+1)]
    res = list(map(list, permutations(arr, m)))

    for i in range(len(res)) :
        print(' '.join(res[i]))
    
nandm()