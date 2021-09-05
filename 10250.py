import math

time = int(input())


def hotel(t) :
    for i in range(t) :
        h, w, p = map(int, input().split())
        if h == 1 :
            head = str(1)
        elif (p % h) == 0 :
            head = str(h)
        else :
            head = str(p % h)
        tail = str(math.ceil(p / h))
        if len(tail) == 1 :
            tail = '0' + tail
        print(int(head + tail))


hotel(time)