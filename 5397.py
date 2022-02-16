import sys

def solution() :
    t = int(sys.stdin.readline())
    
    for _ in range(t) :
        l = sys.stdin.readline().rstrip()
        stack1 = []
        stack2 = []
    
        for s in l :
            if s == '<' :
                if stack1 :
                    stack2.append(stack1.pop())
            elif s == '>' :
                if stack2 :
                    stack1.append(stack2.pop())
            elif s == '-' :
                if stack1 :
                    stack1.pop()
            else :
                stack1.append(s)
        print(''.join(stack1) + ''.join(stack2)[::-1])
solution()