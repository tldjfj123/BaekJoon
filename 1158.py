import sys
from collections import deque
total, num = map(int, sys.stdin.readline().split())

def josephus(t, n) :
    std = deque([i for i in range(1, t+1)])
    res = []
    while 1 :
        for _ in range(n-1) :
            std.append(std.popleft())
        res.append(std.popleft())

        if len(std) == 0 :
            break

    print("<", end='')
    print(str(res)[1:-1], end = '')
    print(">")

        
josephus(total, num)