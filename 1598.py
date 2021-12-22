def tail() :
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    r1 = abs(a//4 - b//4)
    r2 = abs(a%4 - b%4)
    
    print(r1 + r2)
        
tail()