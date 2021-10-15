import sys

def pokemon() :
    n, m = map(int, sys.stdin.readline().split())
    book = dict()

    for i in range(1, n+1) :
        name = input()
        book[str(i)] = name
        book[name] = str(i)

    for _ in range(m) :
        q = sys.stdin.readline().rstrip()
        print(book[q])

pokemon()