def solution() :
    n = int(input())
    order = list(input())
    tmp = [int(input()) for _ in range(n)]
    num = dict()
    op = ['+', '-', '*', '/']
    stack = []
    
    idx = 0
    for i in range(len(order)) :
        if order[i] not in op :
            if order[i] not in num.keys() :
                num[order[i]] = tmp[idx]
                order[i] = tmp[idx]
                idx += 1
            else :
                order[i] = num[order[i]]
             
    for o in order :
        if o not in op :
            stack.append(o)
        else :
            if o == '+' :
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif o == '-' :
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif o == '*' :
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            else :
                a = stack.pop()
                b = stack.pop()
                stack.append(b/a)
    print(f'{stack[0] : >.2f}')
    
solution()