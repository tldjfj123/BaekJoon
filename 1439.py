def turn() :
    arr = list(map(int, input()))
    check0 = 0
    check1 = 0
    
    start = arr[0]
    
    if start == 1 :
        check0 += 1
    else :
        check1 += 1
    
    for i in range(1, len(arr)) :
        if arr[i] != start :
            if start == 0 :
                check0 += 1
            else :
                check1 += 1
            start = arr[i]  
    
    print(min(check0, check1))
          
turn()