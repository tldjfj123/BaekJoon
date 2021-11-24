def library() :
    n, m = map(int, input().split())
    position = list(map(int, input().split()))
    
    position.sort(key = lambda x : abs(x), reverse = True)
    
    plus = []
    minus = []
    
    result = 0
    
    
    for p in position :
        if p > 0 :
            plus.append(p)
        else :
            minus.append(p)
    
    if len(minus) == 0 :
        result += abs(plus[:m][0])
        for i in range(m, len(plus), m) :
            result += abs(plus[i:i+m][0]*2)
            
    elif len(plus) == 0 :
        result += abs(minus[:m][0])
        for i in range(m, len(minus), m) :
            result += abs(minus[i:i+m][0]*2)
            
    else :  
        if abs(plus[:m][0]) >= abs(minus[:m][0]) :
            result += abs(plus[:m][0])
            for i in range(m, len(plus), m) :
                result += abs(plus[i:i+m][0]*2)
            for j in range(0, len(minus), m) :
                result += abs(minus[j:j+m][0]*2)
            
                
        else :
            result += abs(minus[:m][0])
            for i in range(m, len(minus), m) :
                result += abs(minus[i:i+m][0]*2)
            for j in range(0, len(plus), m) :
                result += abs(plus[j:j+m][0]*2)
    print(result)
    
library()