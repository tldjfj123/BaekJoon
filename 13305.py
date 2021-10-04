num = int(input())

def oil(n) :
    length = list(map(int, input().split()))
    price = list(map(int, input().split()))[:-1]
    
    p = 0   # current cursor
    std = 0  
    res = 0

    for i in range(len(price)) :
        if res == 0 :   # set defalt value
            res += price[p] * length[i]
            std = price[i]
        else :
            if price[i] >= std :
                res += std * length[i]
            else :
                std = price[p]
                res += std * length[i]
        p += 1
    print(res)

oil(num)