def tree() :
    h, m = map(int, input().split())
    height = list(map(int, input().split()))

    height.sort(reverse = True)

    left = 0
    right = max(height)

    res = []

    while left <= right :
        mid = (left + right) // 2
        count = 0
        for h in height :
            if h >= mid :
                count += (h - mid)

        if count >= m :
            res.append(mid)
            left = mid + 1
        else :
            right = mid - 1
    
    print(max(res))


tree()