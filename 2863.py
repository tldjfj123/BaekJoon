def fraction() :
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    
    table = [a, b, c, d]
    res = []
    
    for i in range(4) :
        if i == 0 :
            res.append(table[0] / table[2] + table[1] / table[3])
        elif i == 1 :
            res.append(table[2] / table[3] + table[0] / table[1])
        elif i == 2 :
            res.append(table[3] / table[1] + table[2] / table[0])
        else :
            res.append(table[1] / table[0] + table[3] / table[2])
    
    print(res.index(max(res)))
            
fraction()