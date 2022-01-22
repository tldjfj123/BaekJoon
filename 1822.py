def solution() :
    a,b = map(int, input().split())
    arra = set(list(map(int, input().split())))
    arrb = set(list(map(int, input().split())))
    
    calc = arra - arrb
    if len(calc) == 0 :
        print(0)
    else :
        print(len(calc))
        tmp = map(str, sorted(list(calc)))
        print(' '.join(tmp))

solution()