def candy() :
    t = int(input())
    
    for _ in range(t) :
        arr = []
        j, n = map(int, input().split())
        
        for _ in range(n) :
            arr.append(list(map(int, input().split())))
        arr.sort(key = lambda x : x[0]*x[1], reverse = True)
        
        res = 0
        count = 0
        for a in arr :
            count += a[0] * a[1]
            res += 1
            
            if count >= j :
                break
        
        print(res)
            
candy()