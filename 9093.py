import sys

def solution() :
    n = int(input())
    
    for _ in range(n) :
        s= sys.stdin.readline().rstrip()
        words = list(s.split())
        arr = []
        
        for w in words :
            arr.append(w[::-1])
        
        print(' '.join(arr))
        
solution()