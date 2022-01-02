import sys

def alien() :
    n, p = map(int, sys.stdin.readline().split())
    melody = []
    check = []
    
    for _ in range(n) :
        melody.append(list(map(int, sys.stdin.readline().split())))
        check.append(melody[-1][0])
    
    check = list(set(check))
    
    stack = [[] for _ in range(max(check)+1)]
    count = 0
    
    for m in melody :
        if len(stack[m[0]]) == 0 :
            stack[m[0]].append(m[1])
            count += 1
        else :
            if m[1] not in stack[m[0]] :
                if m[1] > stack[m[0]][-1] :
                    stack[m[0]].append(m[1])
                    count += 1
                else :
                    if min(stack[m[0]]) > m[1] :
                        count += len(stack[m[0]])
                        stack[m[0]] = []
                        stack[m[0]].append(m[1])
                        count += 1
                    else :
                        while stack[m[0]][-1] > m[1] :
                            stack[m[0]].pop()
                            count += 1
                        stack[m[0]].append(m[1])
                        count += 1
            else :
                while stack[m[0]][-1] > m[1] :
                    stack[m[0]].pop()
                    count += 1

    print(count)
        
alien()