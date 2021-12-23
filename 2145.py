def play() :
    while 1 :
        n = input()
        if n == "0" :
            break
        n = list(n)
        
        while len(n) != 1 :
            n = list(str(sum(list(map(int, n)))))
            
        print(''.join(n))
    
        
    

play()