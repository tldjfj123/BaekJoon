import sys
import math

fixed, variable, margin =  map(int, sys.stdin.readline().split())

def bep(f, v, m ) :
    if m - v <= 0 :
        return -1
    return int(math.floor(f / (m - v)) + 1)
    
print(bep(fixed, variable, margin))