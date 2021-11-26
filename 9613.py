import math

def sumgcd() :
    t = int(input())
    
    for _ in range(t) :
        tmp = list(map(int, input().split()))
        n, arr = tmp[0], tmp[1:]
        
        total = 0
        
        if len(arr) == 1 :
            print(sum(arr))
            
        else :
            for i in range(len(arr)) :
                for j in range(i+1, len(arr)) :
                    total += math.gcd(arr[i], arr[j])

            print(total)
        
sumgcd()