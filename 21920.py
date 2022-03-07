import math

def solution() :
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    
    total = []
    
    for a in arr :
        if math.gcd(a, x) == 1 :
            total.append(a)
    
    print(sum(total) / len(total))    
    
solution()