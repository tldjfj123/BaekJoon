def camping() :
    count = 1
    while 1 :
        l, p, v = map(int, input().split())
        if l == 0 and p == 0 and v == 0 :
            break
        else :
            if v % p <= l :
                print("Case {}: {}".format(count, (v // p) * l + (v % p)))
            else :
                print("Case {}: {}".format(count, (v // p) * l + l))
        count += 1    
    
camping()