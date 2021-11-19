import sys

def sorting() :
    n = int(sys.stdin.readline())
    s = []
    for _ in range(n) :
        s.append(int(sys.stdin.readline()))
        
    s = sorted(s, reverse=True)
    
    for i in s :
        print(i)
        
sorting()