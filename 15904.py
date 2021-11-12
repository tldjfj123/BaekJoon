def ucpc() :
    s = list(input())
    res = []

    for i in range(len(s)) :
        if s[i] == "U" and len(res) == 0 :
            res.append(s[i])
            
        if s[i] == "C" and len(res) == 1 :
            res.append(s[i])
        
        if s[i] == "P" and len(res) == 2 :
            res.append(s[i])
        
        if s[i] == "C" and len(res) == 3 :
            res.append(s[i])
    
    if len(res) == 4 :
        print("I love UCPC")
    else :
        print("I hate UCPC")
            
ucpc()