def solution() :
    n = input()
    
    i = 0
    while 1 :
        i += 1
        tmp = str(i)
        
        while len(tmp) > 0 and len(n) > 0 :
            if tmp[0] == n[0] :
                n = n[1:]
            tmp = tmp[1:]
        
        if n == '' :
            print(i)
            break

solution()