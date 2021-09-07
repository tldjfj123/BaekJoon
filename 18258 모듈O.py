# 선입 선출!

from collections import deque
import sys

d = deque()

num = int(sys.stdin.readline())

def launch(n) :
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
            d.append(int(tmp[1]))          
        
launch(num)