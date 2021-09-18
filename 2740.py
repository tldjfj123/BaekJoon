def matrix() :
    table1 = []
    table2 = []

    n1, m1 = map(int, input().split())
    for _ in range(n1) :
        table1.append(list(map(int, input().split())))

    n2, m2 = map(int, input().split())
    for _ in range(n2) :
        table2.append(list(map(int, input().split())))
    
    table3 = []
    idx = 0
    for i in range(m2) :
        tmp = []
        for t in table2 :
            tmp.append(t[idx])
        table3.append(tmp)
        idx += 1
    
    for t1 in table1 :
        tmpp = []
        std = t1
        for i in range(len(table3)) :
            std2 = table3[i]
            sum = 0
            for j in range(len(table3[0])) :
                res = std[j] * std2[j]
                sum += res
            tmpp.append(str(sum))
        print(" ".join(tmpp))
            
matrix()