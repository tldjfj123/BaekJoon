def card() :
    n = int(input())
    s = list(map(int, input().split()))
    m = int(input())
    c = list(map(int, input().split()))
    
    s = set(s)
    
    res = []
    
    for i in c :
        if i in s :
            res.append("1")
        else :
            res.append("0")
    
    print(' '.join(res))
            
card()