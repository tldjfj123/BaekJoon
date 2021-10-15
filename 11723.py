import sys

def calcset() :
    res = set()
    num = int(sys.stdin.readline())

    for _ in range(num) :
        order = sys.stdin.readline().split()

        if order[0] == 'add' :
            if int(order[1]) in res :
                continue
            else :
                res.add(int(order[1]))
        elif order[0] == 'remove' :
            if int(order[1]) not in res :
                continue
            else :
                res.remove(int(order[1]))
        elif order[0] == 'check' :
            if int(order[1]) in res :
                print(1)
            else :
                print(0)
        elif order[0] == 'all' :
            res.clear()
            res.update([i for i in range(1, 21)])
        elif order[0] == 'empty' :
            res.clear()
        else :
            if int(order[1]) not in res :
                res.add(int(order[1]))
            else :
                res.remove(int(order[1]))
calcset()