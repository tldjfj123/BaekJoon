# 정수끼리 나눗셈 >> //

import math

def combination() :
    n, m = map(int, input().split())
    calc = math.factorial(n) // (math.factorial(n-m) * math.factorial(m))
    
    print(calc)
    
combination()