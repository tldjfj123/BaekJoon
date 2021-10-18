def pascal() :
    num, idx = map(int, input().split())
    res = []
    for i in range(num) :
        if i == 0 :
            res.append([1])
        elif i == 1 :
            res.append([1, 1])
        else :
            tmp = []
            tmp.append(1)
            target = res[i-1]
            for i in range(len(target)-1) :
                tmp.append((target[i] + target[i+1]))
            tmp.append(1)
            res.append(tmp)
    print(res[num-1][idx-1])

pascal()