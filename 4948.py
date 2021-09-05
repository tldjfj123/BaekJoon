import math

def is_prime_number(x):
    if x == 1 :
        return False
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def prime_list(n):
    if n == 2 :
        return [2]
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           
            for j in range(i+i, n, i): 
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]

def prime_list2(n) :
    if n == 2 :
        return 1
    a = prime_list(n)
    b = prime_list(2*n)
    if is_prime_number(n) == True :
        result = list(set(b) - set(a))
        return len(result) - 1
    else :
        result = list(set(b) - set(a))
        return len(result)


def ber() :
    while 1 :
        n = int(input())
        if n == 0 :
            break
        print(prime_list2(n))
        
ber()