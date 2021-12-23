def polygon() :
    n = int(input())
    
    arr = [0]
    for i in range(1, n) :
        if i == 1 :
            arr.append(2)
        else :
            arr.append(arr[-1] + 3)
    
    print((sum(arr) + (5 * n)) % 45678)
                                       
polygon()