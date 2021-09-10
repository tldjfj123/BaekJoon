from collections import deque
import sys

num = int(sys.stdin.readline())

def queue(n) :
    d = deque([])
    for _ in range(n) :
        f = sys.stdin.readline().rstrip()

        if f == 'pop' :
            if len(d) == 0 :
                print(-1)
            else :
                print(d.popleft())
        elif f == 'size' :
            print(len(d))
        elif f == 'empty' :
            if len(d) == 0 :
                print(1)
            else :
                print(0)
        elif f == 'front' :
            if len(d) == 0 :
                print(-1)
            else :
                print(d[0])
        elif f == 'back' :
            if len(d) == 0 :
                print(-1)
            else :
                print(d[-1])
        else :
            tmp = list(f.split())
            d.append(tmp[1])

queue(num)