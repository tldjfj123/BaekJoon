import sys

num = int(sys.stdin.readline())

def hash(n) :
    res = 0
    arr = list(sys.stdin.readline().rstrip())
    i = 0

    for a in arr :
        res += ((ord(a) - 96) % 31) * (31** i)
        i += 1

    print(res % 1234567891)

hash(num)