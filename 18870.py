import sys

def compression() :
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    
    tmp = sorted(list(set(arr)))
    p = dict()

    for i in range(len(tmp)) :
        p[tmp[i]] = i
    
    res = []
    
    for i in range(len(arr)) :
        res.append(p[arr[i]])
    
    print(' '.join(list(map(str, res))))
    
compression()