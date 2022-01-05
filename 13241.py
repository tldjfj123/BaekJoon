import math
import sys

def lcm() :
    a, b = map(int, sys.stdin.readline().split())
    
    print(math.lcm(a, b))
    
lcm()