import sys
import math
up, down, goal = map(int, sys.stdin.readline().split())

def snail(u, d, g) :
    return math.ceil((g - u) / (u - d)) + 1

print(snail(up, down, goal))