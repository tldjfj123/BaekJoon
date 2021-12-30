def piece() :
    arr = list(input().split())
    
    while sorted(arr) != arr :
        if arr[0] > arr[1] :
            arr[0], arr[1] = arr[1], arr[0]
            print(' '.join(arr))
            
        if arr[1] > arr[2] :
            arr[1], arr[2] = arr[2], arr[1]
            print(' '.join(arr))
            
        if arr[2] > arr[3] :
            arr[2], arr[3] = arr[3], arr[2]
            print(' '.join(arr))
        
        if arr[3] > arr[4] : 
            arr[3], arr[4] = arr[4], arr[3]
            print(' '.join(arr))
        
piece()