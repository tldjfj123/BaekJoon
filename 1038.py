# Maximum : 9876543210
# 첫 수(Head)가 1 부터 시작하면
# 1, 3, 7, 15, 31, 63, 127, 255, 511
from itertools import combinations

def descending() :
    n = int(input())
    res = []
    
    for head in range(1, 10) :
        sub = sorted([str(i) for i in range(head+1)], reverse = True)
        for i in range(len(sub)+1) :
            tmp = list(combinations(sub, i))
            for t in tmp :
                res.append(''.join(t))
                
    result = sorted(list(map(int, sorted(list(set(res)))[2:])))
    
    if n <= len(result) :
        if n == 0 :
            print(0)
        else :
            print(result[n-1])
    else :
        print(-1)
        
descending()