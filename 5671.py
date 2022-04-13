def solution() :
    while 1 :   
        try :
            n, m = map(int, input().split())
            arr = [i for i in range(n, m+1)]
            
            count = 0
            
            for a in arr :
                if len(str(a)) == len(set(str(a))) :
                    count += 1
            print(count)
            
        except :
            break

solution()