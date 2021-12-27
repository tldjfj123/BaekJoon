def wilddog() :
    a, b, c, d = map(int, input().split())
    p, m, n = map(int, input().split())
    
    people = [p, m, n]
    res = []
    
    for p in people :
        count = 0
        for i in range(1, p+1, a+b) :
            if p in range(i, i+a) :
                count += 1
        
        for i in range(1, p+1, c+d) :
            if p in range(i, i+c) :
                count += 1
        print(count)
        
wilddog()