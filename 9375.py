def fashion() :
    n = int(input())
    
    for _ in range(n) :
        closet = dict()
        num = int(input())
        for _ in range(num) :
            name, type = input().split()
            if type in closet.keys() :
                tmp = []
                tmp.append(name)
                for v in closet[type] :
                    tmp.append(v)
                closet[type] = tmp
            else :
                closet[type] = [name]
        
        if len(closet.keys()) == 1 :
            print(len(list(closet.values())[0]))
        else :
            v = list(closet.values())
            
            c = 1
            for i in v :
                c *= (len(i)+1)
            print(c-1)
            
fashion()