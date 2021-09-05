import sys

num = int(sys.stdin.readline())

def repeat(n) :
    for i in range(n) :
        res = []
        t, s = input().split()
        for j in range(len(s)) :
            res.append(s[j] * int(t))
        print(''.join(res))

repeat(num)