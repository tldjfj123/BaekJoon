from itertools import permutations

def solution() :
    a, b = input().split()
    sub = list(map(lambda x : ''.join(x), permutations(a)))
    res = -1
    
    for s in sub :
        if int(b) >= int(s) and s[0] != '0' :
            res = max(res, int(s))
    
    print(res)   
      
solution()