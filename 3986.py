import sys

def goodword() :
    n = int(input())
    
    
    count = 0
    for _ in range(n) :
        s = list(sys.stdin.readline().rstrip())
        stack = []
        
        if len(s) == 1 :
            print(-1)
        else :
            for i in s :
                if not stack or stack[-1] != i :
                    stack.append(i)
                else :
                    stack.pop()
            if not stack :
                count += 1
    
    print(count)
    
goodword()