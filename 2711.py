def miss() :
    t = int(input())
    
    for _ in range(t) :
        idx, s = input().split()
        idx = int(idx)
        s = list(s)
        del s[idx-1]
        
        print(''.join(s))
        
miss()