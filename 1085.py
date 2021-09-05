import math

x, y, w, h = map(int, input().split())

def escape(x, y, w, h) :
    std  = [h-y, w-x, x, y]
    return min(std)

print(escape(x, y, w, h))
