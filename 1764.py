import sys

def dbj() :
    n, m = map(int, input().split())
    d = set()
    b = set()
    for _ in range(n) :
        d.add(sys.stdin.readline().rstrip())
    for _ in range(m) :
        b.add(sys.stdin.readline().rstrip())

    res = []

    for i in d :
        if i in b :
            res.append(i)    

    res.sort()
    
    print(len(res))
    for r in res :
        print(r)
dbj()