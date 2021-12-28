def matrix() :
    n, m = map(int, input().split())
    m1 = []
    m2 = []
    
    for i in range(2) :
        if i == 0 :
            for _ in range(n) :
                tmp = list(map(int, input().split()))
                m1.append(tmp)
        else :
            for _ in range(n) :
                tmp = list(map(int, input().split()))
                m2.append(tmp)
    
    for i in range(n) :
        for j in range(m) :
            m1[i][j] += m2[i][j]
    
    for i in range(n) :
        print(' '.join(map(str, m1[i])))
            
matrix()