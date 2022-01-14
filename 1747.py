import math

def prime(n) :
    m = int(math.sqrt(n))
    
    for i in range(2, m + 1) :
        if n % i == 0 :
            return False
    return True

def solution() :
    n = int(input())
    
    if n == 1 :
        return 2
    
    while 1 :
        if prime(n) == True and str(n) == str(n)[::-1] :
            return n
        else :
            n += 1
        
print(solution())