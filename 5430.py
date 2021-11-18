import sys
from collections import deque

def ac() :
    t = int(sys.stdin.readline())
    
    for _ in range(t) :
        check = 0
        p = list(sys.stdin.readline().rstrip())
        n = int(sys.stdin.readline())

        s = sys.stdin.readline().rstrip()
            
        if s == "[]" :
            arr = []
        else :
            arr = deque(list(s[1:-1].split(",")))
            
        rcheck = 0
        
        for order in p :
            if order == "R" :
                rcheck += 1
            else :
                if len(arr) == 0 :
                    print("error")
                    check += 1
                    break
                else :
                    if rcheck % 2 == 1 :
                        arr.pop()
                    else :
                        arr.popleft()
        
        if check == 0 :
            if rcheck % 2 == 0 :
                print("[" + ','.join(list(arr)) +"]")
            else :
                print("[" + ','.join(list(reversed(arr))) +"]")
ac()