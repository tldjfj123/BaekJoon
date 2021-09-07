i = list(map(int, input().split()))
i.sort()

if i[1] - i[0] == i[2] - i[1] :
    print(i[2] + i[2] - i[1])
else :
    if i[2] - i[1] > i[1] - i[0] :
        print(i[2] - (i[1] - i[0]))
    else :
        print(i[1] - (i[2] - i[1]))