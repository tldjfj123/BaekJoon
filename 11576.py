def bc() :
    a, b = map(int, input().split())
    n = int(input())
    arr = list(map(int, input().split()))
    
    tmp = 0
    
    for i in range(len(arr)) :
        tmp += (arr.pop() * a ** i)
    
    res = []
    while tmp != 0 :
        t = tmp % b
        res.append(str(t))
        tmp //= b
    
    res = res[::-1]
    print(' '.join(res))        

bc()