import sys

num = int(sys.stdin.readline())

def conference(n) :
    time = []
    count = 0
    
    for _ in range(n) :
        start, end = sys.stdin.readline().split()
        time.append((int(start), int(end)))

    timetable = [False] * (max(time)[1] + 1)

    time.sort(key = lambda x : (x[1], x[0]))

    for t in time :
        if t[0] == t[1] :
            count += 1
            continue
        if sum(timetable[t[0] : t[1]+1]) == 0 :
            for i in range(t[0], t[1]) :
                timetable[i] =True
            count += 1
    print(count)  

conference(num)        