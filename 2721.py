def triangle() :
    t = int(input())
    
    for _ in range(t) :
        n = int(input())
        arr = [i for i in range(1, n+2)]

        res = 0     
        for i in range(n) :
            res += (arr[i] * sum(arr[:i+2]))
        
        print(res)
triangle()