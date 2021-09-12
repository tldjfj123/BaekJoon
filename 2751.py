import sys

num = int(sys.stdin.readline())

def sorting(n) :
    table = []
    for _ in range(n) :
        i = int(sys.stdin.readline())
        table.append(i)
    table.sort()

    for i in table :
        print(i)


sorting(num)