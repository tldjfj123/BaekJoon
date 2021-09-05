import sys

num = int(sys.stdin.readline())

def calc(n) :
    arr =list(map(int, sys.stdin.readline().split()))
    arr.sort()
    print('{} {}'.format(arr[0], arr[n-1]))

calc(num)