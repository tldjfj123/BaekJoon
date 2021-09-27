import sys

num = int(sys.stdin.readline())

def summary(n) :
    s = 0
    count = 0
    number = 1
    while 1 :
        s += number
        count += 1
        number += 1
        if n - s < number :
            break
    print(count)

summary(num)