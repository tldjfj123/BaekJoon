def prime(n) :
    res = [True for _ in range(n+1)]
    
    m = int(n ** 0.5)
    for i in range(2, m+1) :
        if res[i] == True :
            for j in range(i + i, n, i) :
                res[j] = False
    
    return [i for i in range(2, n+1) if res[i] == True]
                
def restore() :
    t = int(input())
    
    for _ in range(t) :
        n = int(input())
        table = prime(n)
        
        idx = 0
        count = 0
        
        while n != 1 :
            if n % table[idx] == 0 :
                n //= table[idx]
                count += 1
            else :
                if count > 0 :
                    print(f"{table[idx]} {count}")
                idx += 1
                count = 0
        print(f"{table[idx]} {count}")
            
restore()