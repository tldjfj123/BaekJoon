import sys

def sorting() :
    n = int(sys.stdin.readline())
    arr = []
    for _ in range(n) :
        arr.append(int(sys.stdin.readline()))
    
    arr = sorted(arr)
    
    for i in arr :
        print(i)
        
sorting()