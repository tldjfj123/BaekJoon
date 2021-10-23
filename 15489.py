def pascal() :
    r, c, w = map(int, input().split())
    arr = []
    s = 0

    for i in range(0, 30) :
        if i == 0 :
            arr.append([1])
        else :
            tmp = []
            tmp.append(1)
            for j in range(len(arr[i-1])-1) :
                tmp.append(arr[i-1][j] + arr[i-1][j+1])
            tmp.append(1)
            arr.append(tmp)

    if w == 1 :
        idx = 1
        for i in range(r-1, r+w) :
            s += sum(arr[i][c-1:c-1+idx])
            idx += 1
        print(s)

    else :
        idx = 1
        for i in range(r-1, r+w-1) :
            s += sum(arr[i][c-1:c-1+idx])
            idx += 1
        print(s)

pascal()