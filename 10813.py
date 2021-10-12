def ball() :
    n, m = map(int, input().split())

    arr = [i for i in range(1, n+1)]
    for _ in range(m) :
        f, b = map(int, input().split())
        arr[f-1], arr[b-1] = arr[b-1], arr[f-1]
    print(' '.join(list(map(str, arr))))

ball()