import sys

def solution() :
    n = int(sys.stdin.readline())
    arr = []
    
    for _ in range(n) :
        arr.append(sys.stdin.readline().rstrip())
    
    for a in arr :
        if a[::-1] in arr :
            return f'{len(a)} {a[len(a) // 2]}' 

print(solution())