import math
import sys

start, finish = map(int, sys.stdin.readline().split())

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
    for i in range(s, f+1) :
        if is_prime_number(i) == True :
            print(i)
    

prime(start, finish)