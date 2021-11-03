import sys

def overflow() :
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    res = 1

    for i in range(len(arr)) :
        res *= (arr[i] % m)
    
    print(res % m)

overflow()