from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split()) 

def josephus(n, k) :
    result = []
    d = deque([i for i in range(1, n + 1)])
    while 1 :
        for _ in range(k-1) :
            tmp = d.popleft()
            d.append(tmp)
        tmp2 = d.popleft()
        result.append(tmp2)
        if len(d) == 0 :
            break
    print('<'+', '.join(map(str, result)) + '>')
        
josephus(n, k)