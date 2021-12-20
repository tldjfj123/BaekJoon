def basketball() :
    n = int(input())
    
    res = []
    
    check = 0
    for _ in range(n) :
        player = input()[0]
        res.append(player)
    
    sub = list(set(res))
    
    fin = []
    for s in sub :
        if res.count(s) >= 5 :
            check += 1
            fin.append(s)
    
    if check == 0 :
        print("PREDAJA")
    else :
        fin = sorted(fin)
        print(''.join(fin))

basketball()