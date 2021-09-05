import math

start = int(input())
finish = int(input())

def is_prime_number(x) :
    if x == 0 :
        return False
    elif x == 1 :
        return False
    else :
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False 
        return True 

def prime(s, f) :
    sum = 0
    arr = []
    for i in range(s, f+1) :
        if is_prime_number(i) == True :
            sum += i
            arr.append(i)
    if len(arr) == 0 :
        print(-1)
    else :
        print(sum)
        print(min(arr))

prime(start, finish)