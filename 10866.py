from collections import deque
import sys

num = int(sys.stdin.readline())

def d(n) :
    items = deque([])
    for _ in range(n) :
        f = sys.stdin.readline().rstrip()
        if f == 'pop_front' :
            if len(items) == 0 :
                print(-1)
            else :
                print(items.popleft())
        elif f == 'pop_back' :
            if len(items) == 0 :
                print(-1)
            else :
                print(items.pop())
        elif f == 'size' :
            print(len(items))
        elif f == 'empty' :
            if len(items) == 0 :
                print(1)
            else :
                print(0)
        elif f == 'front' :
            if len(items) == 0 :
                print(-1)
            else :
                print(items[0])
        elif f == 'back' :
            if len(items) == 0 :
                print(-1)
            else :
                print(items[-1])
        else :
            arr = list(f.split())
            if arr[0] == 'push_front' :
                items.appendleft(arr[1])
            if arr[0] == 'push_back' :
                items.append(arr[1])

d(num)