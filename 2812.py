import sys
from collections import deque
def solution() :
    n, k = map(int, sys.stdin.readline().split())
    num = deque(list(input()))
    
    alive = []
    dead = []
    
    while len(dead) != k :
        if len(num) == 0 :
            for _ in range(k - len(dead)) :
                alive.pop()
            break
        if len(alive) == 0 :
            alive.append(num.popleft())
        else :
            if alive[-1] >= num[0] :
                alive.append(num.popleft())
            else :
                dead.append(alive.pop())
    
    print(''.join(alive + list(num)))
                
solution()