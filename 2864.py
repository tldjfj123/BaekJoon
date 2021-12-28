def embarass() :
    a, b = input().split()
    a = list(a)
    b = list(b)
    
    res = []
    
    for i in range(2) :
        # max
        if i == 1 :
            for i in range(len(a)) :
                if a[i] == "5" :
                    a[i] = "6"
            
            for i in range(len(b)) :
                if b[i] == "5" :
                    b[i] = "6"

            res.append(int(''.join(a)) + int(''.join(b)))
            
        # min
        else :
            for i in range(len(a)) :
                if a[i] == "6" :
                    a[i] = "5"
            
            for i in range(len(b)) :
                if b[i] == "6" :
                    b[i] = "5"
                    
            res.append(int(''.join(a)) + int(''.join(b)))
            
    print(" ".join(map(str, res)))
    
embarass()