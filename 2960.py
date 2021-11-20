from collections import deque

def sieve() :
    n, k = map(int, input().split())

    arr = [i for i in range(2, n+1)]
    
    removed = []
    
    while arr :
        p = min(arr)
        for i in arr :
            if i % p == 0 :
                arr.remove(i)
                removed.append(i)
        if len(arr) >= k :
            break
    print(removed[k-1])
                
sieve()