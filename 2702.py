import math

def m() :
    n = int(input())
    
    for _ in range(n) :
        a, b = map(int, input().split())
        print(f"{math.lcm(a, b)} {math.gcd(a, b)}")

m()