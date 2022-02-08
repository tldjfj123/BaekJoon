def solution() :
    n = int(input())
    std = list(input())
    
    for _ in range(n-1) :
        compare = list(input())
        for j in range(len(std)) :
            if std[j] != compare[j] :
                std[j] = '?'
    
    print(''.join(std))
                
solution()