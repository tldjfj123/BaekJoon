import sys

num = int(sys.stdin.readline())

def sequence(n) :
    cur = 1
    check = True
    stack = []
    res = []

    for _ in range(n) :
        i = int(sys.stdin.readline())
        while cur <= i :
            stack.append(cur)
            res.append('+')
            cur += 1
        if stack[-1] == i :
            stack.pop()
            res.append('-')
        else :
            check = False

    if check == False :
        print("NO")
    else :
        for result in res :
            print(result)
    
sequence(num)