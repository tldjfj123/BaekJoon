def printer() :
    arr = []
    for i in range(9) :
        arr.append(int(input()))
    value = max(arr)
    idx = arr.index(value)
    print('{}\n{}'.format(value, idx+1))
    return('{}\n{}'.format(value, idx+1))

printer()