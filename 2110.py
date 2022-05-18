def count(len, n, arr) :
    cnt = 1
    end = arr[0]
    for i in range(1, n) :
        if arr[i] - end >= len :
            cnt += 1
            end = arr[i]
    return cnt
    
def solution() :
    n, c = map(int, input().split())
    p = [int(input()) for _ in range(n)]

    p.sort()
    
    res = 0
    left = 1
    right = p[n-1]
    
    while left <= right :
        mid = (left + right) // 2
        if count(mid, n, p) >= c :
            res = mid
            left = mid + 1
        else :
            right = mid - 1
    print(res)
         
solution()