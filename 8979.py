import sys

def olympic() :
    n, target = map(int, sys.stdin.readline().split())
    scoreboard = []
    
    for _ in range(n) :
        scoreboard.append(list(map(int, sys.stdin.readline().split())))
    
    scoreboard.sort(key = lambda x : (-x[1], -x[2], -x[3]))

    for i in range(n) :
        if scoreboard[i][0] == target :
            idx = i
    
    for i in range(n) :
        if scoreboard[idx][1 : ] == scoreboard[i][1 : ] :
            print(i + 1)
            break

olympic()