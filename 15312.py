def name() :
    alphabet = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
    names = []
    for _ in range(2) :    
        names.append(list(input()))
    arr = []
    for i in range(len(names[0])) :
        arr.append(names[0][i])
        arr.append(names[1][i])

    arr = list(map(lambda x : ord(x) - 65, arr)) 
    arr = [alphabet[i] for i in arr]

    while len(arr) >= 3 :
        res = []
        for i in range(len(arr)-1) :
            calc = arr[i] + arr[i+1]
            if calc >= 10 :
                res.append(calc % 10)
            else :
                res.append(calc)
        arr = res
    print(''.join(list(map(str, arr))))

name()