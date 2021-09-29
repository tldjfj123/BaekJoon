import math

num = int(input())

def bridge(n) :
    for _ in range(n) :
        tmp = list(map(int, input().split()))
        a = max(tmp)
        b = min(tmp)
        print(int(math.factorial(a) / (math.factorial(a-b) * math.factorial(b))))

bridge(num)