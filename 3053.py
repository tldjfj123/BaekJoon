import math

num = int(input())

def s(n) :
    euclid = math.pi * n * n
    taxi = math.sqrt(n**2 + n**2) * math.sqrt(n**2 + n**2)
    print(round(euclid, 6))
    print(round(taxi, 6))

s(num)