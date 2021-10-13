import sys
def lan() :
    k, n = map(int, input().split())
    arr = [int(sys.stdin.readline()) for _ in range(k)]
    arr.sort(reverse = True)
    
    res = []
    left = 1
    right = arr[0]

    while left <= right :
        mid = (left + right) // 2
        count = 0
        
        for a in arr :
            count += a // mid
        
        if count >= n :
            res.append(mid)
            left = mid + 1
        else :
            right = mid - 1
    print(max(res))
    
lan()