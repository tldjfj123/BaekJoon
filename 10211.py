def ms() :
    t = int(input())
    
    for _ in range(t) :
        n = int(input())
        arr = list(map(int, input().split()))
        
        res = []
        for i in range(n) :  # 0 ~ 4
            for j in range(i, n) : 
                res.append(sum(arr[i:j+1]))
        
        print(max(res))
            
ms()