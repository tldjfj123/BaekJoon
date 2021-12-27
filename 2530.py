def oven() :
    a, b, c = map(int, input().split())
    d = int(input())
    
    s = d % 60
    m = (d // 60) % 60
    h = (d // 3600) % 24
    
    c += s
    if c >= 60 :
        m += 1
        c %= 60
    
    b += m
    if b >= 60 :
        h += 1
        b %= 60
    
    a += h
    if a >= 24 :
        a %= 24
    
    print(f"{a} {b} {c}")
    
oven()
