# // 2
# μμμ 1 λΊ

def atob() :
    a, b = map(int, input().split())
    
    count = 1
    
    while b != a :
        if (b % 2 != 0) and (b % 10 != 1) or (b < a) :
            count = -1
            break
        
        else :
            if b % 10 == 1 :
                b //= 10
                count += 1
            else :
                b //= 2
                count += 1
    
    print(count)
    
atob()