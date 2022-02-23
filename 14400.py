import sys

def solution() :
    n = int(sys.stdin.readline())
    locations = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    mid_x = sorted(locations, key = lambda x : x[0])[n // 2][0]
    mid_y = sorted(locations, key = lambda x : x[1])[n // 2][1]
    
    res = 0
    
    for l in locations :
        res += (abs(mid_x - l[0]) + abs(mid_y - l[1]))
    
    print(res)
    
solution()