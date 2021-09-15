import sys

num = int(sys.stdin.readline())

def conference(n) :
    time = []
    count = 0

    for _ in range(n) :
        start, end = sys.stdin.readline().split()
        time.append([int(start), int(end)])
    
    time.sort(key = lambda x : (x[1], x[0]))

    start = 0

    for t in time :
        if t[0] >= start :
            start = t[1]
            count += 1
    print(count)

conference(num)