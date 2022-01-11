def sumofnum() :
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    res = 0
    left = 0
    right = 0
    
    while right < n and left < n :
        if sum(arr[left : right + 1]) < m :
            right += 1
        elif sum(arr[left : right + 1]) == m :
            res += 1
            if left < right :
                left += 1
            else :
                right += 1
        else :
            left += 1
    
    print(res)
sumofnum()