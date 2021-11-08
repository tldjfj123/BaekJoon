def multiple() :
    arr = list(map(int, list(input())))
    count = 0

    while len(arr) > 1 :
        arr =  list(map(int, list(str(sum(arr)))))
        count += 1

    print(count)
    if sum(arr) % 3 == 0 :
        print("YES")
    else :
        print("NO")
    
multiple()