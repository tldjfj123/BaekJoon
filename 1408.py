def twentyfour() :
    now = list(map(int, input().split(":")))
    start = list(map(int, input().split(":")))
    
    s = start[2] - now[2]
    m = start[1] - now[1]
    h = start[0] - now[0]
    
    if s < 0 :
        s += 60
        m -= 1
    if m < 0 :
        m += 60
        h -= 1
    if h < 0 :
        h += 24
    
    if len(str(s)) == 1 :
        s = "0" + str(s)
    
    if len(str(m)) == 1 :
        m = "0" + str(m)
    
    if len(str(h)) == 1 :
        h = "0" + str(h)
    
    print("{}:{}:{}".format(h, m, s))    
        
twentyfour()