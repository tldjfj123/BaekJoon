import sys

def minecraft() :
    # Remove block : 2초
    # Insert block 1초
    # Print total time and maximum height of ground
    
    n, m, b = map(int, sys.stdin.readline().split())
    ground = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    res = []
    for height in range(257) :
        dig = 0
        ins = 0

        for i in range(n) :
            for j in range(m) :
                if ground[i][j] <= height :
                    ins += height - ground[i][j]
                else :
                    dig += (ground[i][j] - height)
        block = dig + b

        if block < ins :
            continue

        time = 2 * dig + ins
        res.append((time, height))

    res.sort(key = lambda x : (x[0], -x[1]))
    print("{} {}".format(res[0][0], res[0][1]))  
        
minecraft()