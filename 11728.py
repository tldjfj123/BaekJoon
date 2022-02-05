import sys

def solution() :
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    res = []
    
    a_idx = 0
    b_idx = 0
    while len(a) != a_idx or len(b) != b_idx :
        if len(a) == a_idx :
            res.append(b[b_idx])
            b_idx += 1
        elif len(b) == b_idx :
            res.append(a[a_idx])
            a_idx += 1
        else :
            if a[a_idx] < b[b_idx] :
                res.append(a[a_idx])
                a_idx += 1
            else :
                res.append(b[b_idx])
                b_idx += 1
    
    for r in res :
        print(r, end = ' ')
solution()