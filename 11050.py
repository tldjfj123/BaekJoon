import math

a, b = map(int, input().split())

def coefficient(a, b) :
    return int(math.factorial(a) / (math.factorial(a-b) * math.factorial(b)))

print(coefficient(a, b))