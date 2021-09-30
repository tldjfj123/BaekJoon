import sys

num = int(input())

def divisor(n) :
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    print(arr[0] * arr[-1])

divisor(num)