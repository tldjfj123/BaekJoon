import sys

def solution() :
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    
    prefix = [0 for _ in range(n+1)]
    
    for i in range(1, n+1) :
        prefix[i] = prefix[i-1] + arr[i-1]
     
    m = int(sys.stdin.readline())
    
    for _ in range(m) :
        a, b = map(int, sys.stdin.readline().split())
        print(prefix[b] - prefix[a-1])

solution()