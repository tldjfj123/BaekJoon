import math

def total() :
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    
    x, y = a*d + b*c, b*d
    
    if math.gcd(x, y) == 1 :
        print(x, y)
    else :
        print(x // math.gcd(x, y), y // math.gcd(x, y)) 

total()