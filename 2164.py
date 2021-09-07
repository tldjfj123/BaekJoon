import sys
from collections import deque

num = int(sys.stdin.readline())

def card(n) :
    d = deque([i for i in range(1, n + 1)])
    while 1 :
        if len(d) > 1 :
            d.popleft()
            d.append(d.popleft())
        else :
            break
    return sum(d)
print(card(num))

