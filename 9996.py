import sys

def solution() :
    n = int(sys.stdin.readline())
    std = sys.stdin.readline().rstrip().split('*')
    
    for _ in range(n) :
        f = list(sys.stdin.readline().rstrip())
        
        if ''.join(f[ : len(std[0])]) > std[0] :
            print('NE')
            continue
        
        if ''.join(f[-len(std[1]) : ]) > std[1] :
            print('NE')
            continue        
        
        if ''.join(f[ : len(std[0])]) != std[0] :
            print('NE')
            continue
        else :
            for i in range(0, len(std[0])) :
                f[i] = ''
        
        if ''.join(f[-len(std[1]) : ]) != std[1] :
            print('NE')
        else :
            print('DA') 
            
solution()