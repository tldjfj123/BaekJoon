import sys

num = int(sys.stdin.readline())

def beacon(n) :
    table = []
    for _ in range(n) :
        x, y = map(int, sys.stdin.readline().split())
        table.append((x, y))
    table.sort(key = lambda x : (x[1], x[0]))

    for t in table :
        print(t[0], end = ' ')
        print(t[1])

beacon(num)