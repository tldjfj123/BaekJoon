import sys

num = int(input())

def vps(n) :
    for _ in range(n) :
        items = []
        s = sys.stdin.readline().rstrip()
        if s[0] == ')' :
            print("NO")
            continue
        for word in s :
           items.append(word)
           if len(items) >= 2 and items[-2] == '(' and items[-1] == ')' :
               items.pop()
               items.pop()
        if len(items) == 0 :
            print("YES")
        else :
            print("NO")
            
vps(num)