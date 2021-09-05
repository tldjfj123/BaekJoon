import sys

num = int(sys.stdin.readline())

def hive(n) :
    if n == 1 :
        return 1
    floor = [1]
    t = 0
    idx = 0
    while 1 :
        t += 6
        floor.append(floor[idx] + t)
        if n <= floor[-1] :
            return len(floor)
        idx += 1

print(hive(num))