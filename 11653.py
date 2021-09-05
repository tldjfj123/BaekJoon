import sys

num = int(sys.stdin.readline())

def factorization(n) :
    std = 2
    while 1 :
        s, r = divmod(n, std)
        if r == 0 :
            print(std)
            if s == 1 :
                break
            else :
                n = s
        else :
            if s == 0 and r == 1 :
                break
            std += 1

factorization(num)