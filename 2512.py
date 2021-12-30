def budget() :
    n = int(input())
    request = list(map(int, input().split()))
    budget = int(input())
    
    left = 0
    right = max(request)
    
    res = 0
    
    while left <= right :
        center = (left + right) // 2
        total = 0
        for i in request :
            if i > center :
                total += center
            else :
                total += i
                
        if total <= budget :
            res = center
            left = center + 1
        else :
            right = center - 1
        
    print(res)
        
budget()