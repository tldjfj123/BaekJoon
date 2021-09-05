def rectangle() :
    xs = []
    ys = []
    xc = 0
    yc = 0
    for i in range(3) :
        x, y = map(int, input().split())
        xs.append(x)
        ys.append(y)
    xs.sort()
    ys.sort()

    if xs[0] == xs[1] :
        xc += max(xs)
    else :
        xc += min(xs)

    if ys[0] == ys[1] :
        yc += max(ys)
    else :
        yc += min(ys)

    print(xc, yc)

rectangle()