def solution() :
    n = int(input())
    target = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    res = 0
    left = 0
    right = n-1
    
    while left < right :
        if arr[left] + arr[right] == target :
            res += 1
            left += 1
            right -= 1
        elif arr[left] + arr[right] > target :
            right -= 1
        else :
            left += 1
    
    print(res)
    
solution()