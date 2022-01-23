import sys

def phone() :
    t = int(sys.stdin.readline())
    
    for _ in range(t) :
        n = int(sys.stdin.readline())
        pb = []
        for _ in range(n) :
            pb.append(sys.stdin.readline().rstrip())
        
        pb.sort()
        
        for i in range(len(pb)-1) :
            if len(pb[i]) < len(pb[i+1]) :
                if pb[i+1][:len(pb[i])] == pb[i] :
                    print('NO')
                    break
        else :
            print('YES')
        
phone()