def calendar() :
    e, s, m = map(int, input().split())
    
    count = 0
    
    if e == 1 and s == 1 and m == 1 :
        return 1
    
    arr = [1, 1, 1]
    
    while 1 :
        arr[0] += 1
        arr[1] += 1
        arr[2] += 1
        
        count += 1
        
        if arr[0] == 16 :
            arr[0] = 1
        if arr[1] == 29 :
            arr[1] = 1
        if arr[2] == 20 :
            arr[2] = 1
          
        if arr[0] == e and arr[1] == s and arr[2] == m :
            return count + 1
        
print(calendar())