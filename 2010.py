import sys

def plug() :
    n = int(input())
    multitap = []
    
    for _ in range(n) :
        t = int(sys.stdin.readline())
        multitap.append(t)
    
    print(sum(multitap) - (n-1))

plug()