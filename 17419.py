import sys

def beat() :
    n = int(sys.stdin.readline())
    k = sys.stdin.readline().rstrip()
    
    res = 0
    for i in k :
        if i == "1" : 
            res += 1
            
    print(res)
    
beat()