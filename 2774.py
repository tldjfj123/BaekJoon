def beauty() :
    t = int(input())
    
    for _ in range(t) :
        x = list(input())
        print(len(set(x)))

beauty()