from itertools import combinations

def solution() :
    l, c = map(int ,input().split())
    arr = sorted(input().split())
    sub = list(combinations(arr, l))
    
    for s in sub :
        c = 0
        v = 0
        
        for i in s :
            if i in "aeiou" :
                v += 1
            else :
                c += 1
        
        if v >= 1 and  c >= 2 :
            print(''.join(s))

solution()