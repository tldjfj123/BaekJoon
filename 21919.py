import sys
import math

def primeList(n : int) :
    prime = [True] * (n+1)
    prime[1] = False
    m = int(math.sqrt(n))
    
    for i in range(2, m+1) :
        if prime[i] == True :
            for j in range(i+i, n+1, i) :
                prime[j] = False

    return [i for i in range(2, n+1) if prime[i]]    

def solution() :
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    
    tmp = primeList(max(nums))
    res = []
    for n in nums :
        if n in tmp :
            res.append(n)
    
    if not res :
        print(-1)
    else :
        calc = res[0]
        for r in res :
            calc = (r * calc) // math.gcd(r, calc)
        print(calc)
        
solution()