import sys

def solution() :
    n, m = map(int, sys.stdin.readline().split())
    bottles = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    
    left = 1
    right = max(bottles)
    res = 0
    
    while left <= right :
        mid = (left + right) // 2
        tmp = sum([b // mid for b in bottles])

        if tmp >= m :
            res = mid
            left = mid + 1
        else :
            right = mid - 1
    
    print(res)
            
solution()