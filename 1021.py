from collections import deque
import math
#1. popleft 
#2. popleft and append
#3. pop and appendleft

def q() :
    
    n, m = map(int, input().split())
    goal = list(map(int, input().split()))
    arr = deque([i for i in range(1, n+1)])
     
    count = 0
    
    for i in range(len(goal)) :
        std = goal[i]       
        while 1 :
            midx = math.floor(len(arr)/2)
            if arr[0] == std :
                arr.popleft()
                break
            else :
                if arr.index(std) <=  midx:
                    arr.append(arr.popleft())
                    count += 1
                else :
                    arr.appendleft(arr.pop())
                    count += 1    
    print(count)
q()