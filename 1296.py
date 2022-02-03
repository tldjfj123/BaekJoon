import sys

def solution() :
    y = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    std = list('LOVE')
    
    if n == 1 :
        print(sys.stdin.readline().rstrip())
    else :
        res = []
        for _ in range(n) :
            s = sys.stdin.readline().rstrip()
                
            calc = 1
            for i in range(len(std)) :
                for j in range(i+1, len(std)) :
                    calc *= (y.count(std[i]) + s.count(std[i])) + (y.count(std[j]) + s.count(std[j]))
            
            res.append((calc % 100, s))
        
        res.sort(key = lambda x : (-x[0], x[1]))

        print(res[0][1])
                                 
solution()