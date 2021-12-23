def continuous() :
    for _ in range(3) :
        n = list(input())
        count = []
        check = 0
        for i in range(1, len(n)) :
            if n[i-1] == n[i] :
                check += 1
            else :
                count.append(check)
                check = 0
        count.append(check)
        print(max(count)+1)
            
continuous()