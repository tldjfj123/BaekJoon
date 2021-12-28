def system() :
    string, n = input().split()
    n = int(n)
        
    if n > 10 :
        alpha = n - 10
        table = [str(i) for i in range(10)]
        
        for i in range(alpha) :
            table.append(chr(i+65))
        
    else :
        table = [str(i) for i in range(n)]
    
    exponent = len(string)-1
    res = 0
    
    for s in string :
        res += table.index(s) * (n ** exponent)
        exponent -= 1
    
    print(res)
          
system()