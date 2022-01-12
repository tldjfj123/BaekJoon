from itertools import permutations

def solution() :
    n = int(input())
    arr = list(map(int, input().split()))
    
    sub = list(permutations(arr, n))
    sub = list(map(lambda x : list(x), sub))
    
    res = []
    for s in sub :
        total = 0
        for i in range(1, len(s)) :
            total += abs(s[i-1] - s[i])
        res.append(total)
    
    print(max(res))    

solution()