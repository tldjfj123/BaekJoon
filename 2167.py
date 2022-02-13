import sys

def solution() :
    n, m = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    k = int(sys.stdin.readline())
    
    for _ in range(k) :
        i, j, x, y = map(int, sys.stdin.readline().split())
        s = 0
        for a in range(i, x+1) :
            for b in range(j, y+1) :
                s += arr[a-1][b-1]
        print(s)
                
solution()