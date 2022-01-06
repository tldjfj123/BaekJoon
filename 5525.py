import sys

def ioi() :
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    s = sys.stdin.readline().rstrip()
    
    count = 0
    res = 0
    stack = []
    
    for i in range(m) :
        if s[i] == 'O' :
            continue
        else :
            stack.append(i)
    
    for i in range(1, len(stack)) :
        if stack[i] - stack[i-1] == 2 :
            count += 1
        else :
            count = 0
        
        if count >= n :
            res += 1
        
    print(res)
            
ioi()