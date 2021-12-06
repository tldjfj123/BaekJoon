import math

def test() :
    n = int(input())
    a = list(map(int, input().split()))
    b, c = map(int, input().split())
    
    count = 0
    
    for i in a :
        if i <= b :
            count += 1
        else :
            if i-b <= c :
                count += 1
            else :
                count += (math.ceil((i-b) / c))
            count += 1
    
    print(count)
            
test()