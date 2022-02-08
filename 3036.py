import math

def solution() :
    n = int(input())
    r = list(map(int, input().split()))
    
    for i in range(1, n) :
        t = math.gcd(r[0], r[i])
        print(f'{r[0] // t}/{r[i] // t}')
        
solution()