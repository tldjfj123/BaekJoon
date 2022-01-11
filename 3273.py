def solution() :
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    
    arr.sort()
    
    left = 0
    right = n-1
    res = 0
    
    while left < right :
        calc = arr[left] + arr[right]
        
        if calc == x :
            res += 1
        
        if calc < x :
            left += 1
        else :
            right -= 1

    print(res)
    
solution()