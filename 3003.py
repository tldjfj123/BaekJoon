def chess() :
    arr = [1, 1, 2, 2, 2, 8]
    found = list(map(int, input().split()))

    res = [str(arr[i] - found[i]) for i in range(6)]

    print(' '.join(res))
chess()