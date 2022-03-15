import sys

def solution() :
    stack1 = list(sys.stdin.readline().rstrip())
    stack2 = []
    n = int(sys.stdin.readline())
    
    for _ in range(n) :
        order = sys.stdin.readline().rstrip().split()
        if order[0] == "P" :
            stack1.append(order[1])
        elif order[0] == "L" and stack1 != [] :
            stack2.append(stack1.pop())
        elif order[0] == "D" and stack2 != [] :
            stack1.append(stack2.pop())
        elif order[0] == "B" and stack1 != [] :
            stack1.pop()
    print("".join(stack1 + list(reversed(stack2))))            

solution()