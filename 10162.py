num = int(input())

def microwave(n) :
    time = [300, 60, 10]
    res = []
    while 1 :
        
        for t in time :
            count = 0
            if n // t > 0 :
                count += n // t
                n -= t * (n // t)
            res.append(count)
        
        if n == 0 :
            for r in res :
                print(r, end = ' ')
            break
        else :
            print(-1)
            break
  
microwave(num)