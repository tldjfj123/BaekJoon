import sys

def seven() :
    n = int(sys.stdin.readline())
    score = [float(sys.stdin.readline()) for _ in range(n)]
    
    score.sort()
    
    for i in range(7) :
        print(f'{score[i]:.3f}')

seven()