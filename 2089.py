def reversebinary() :
    n = int(input())
    
    if n == 0 :
        print(0)    
    elif n == 1 :
        print(str(1))
    else :
        res = []
        while 1 :
            if n == -1 :
                res.append(str(1))
                res.append(str(1))
                break
            elif n == 1 :
                res.append(str(1))
                break
                
            if n > 0 :
                if n % 2 == 1 :
                    n = -(n // 2)
                    res.append(str(1))
                else :
                    n = -(n // 2)
                    res.append(str(0))
            else :
                if n % 2 == 1 :
                    n = (abs(n) // 2) + 1
                    res.append(str(1))
                else :
                    n = (abs(n) // 2)
                    res.append(str(0))
                    
        print(''.join(res[::-1]))        

reversebinary()