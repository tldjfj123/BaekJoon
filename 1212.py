def calc() :
    s = input()
    arr = list(map(int, list(s)))
    res = []

    for i in range(len(arr)) :
        res.append(bin(arr[i]))
    
    res[0] = res[0].replace("0b", "")
    
    for i in range(1, len(res)) :
        if len(res[i]) == 3 :
            res[i] = res[i].replace("0b", "00")
        elif len(res[i]) == 4 :
            res[i] = res[i].replace("0b", "0")
        elif len(res[i]) == 5 :
            res[i] = res[i].replace("0b", "")

    print("".join(res))
    
calc()