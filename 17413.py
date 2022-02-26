import sys

def solution() :
    s = sys.stdin.readline().rstrip()
    stack1 = [] # forward order
    stack2 = [] # reverse order
    switch = False
    
    for s in s :
        if s == '<' :
            if stack2 :
                stack1 = stack1 + stack2[::-1]
                stack2 = []
            switch = True
            stack1.append(s)
        elif s == '>' :
            switch = False
            stack1.append(s)
        else :
            if switch == True :
                stack1.append(s)
            else :
                if s == ' ' :
                    stack1 = stack1 + stack2[::-1]
                    stack2 = []
                    stack1.append(s)
                else :
                    stack2.append(s)
    
    if not stack2 :
        print(''.join(stack1))
    else :
        print(''.join(stack1 + stack2[::-1]))
    
solution()