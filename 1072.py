def calc(x : int, y : int) -> int :
    return ((y * 100) // x)

def game() :
    x, y = map(int, input().split())
    res = []
    std = calc(x, y)
    
    if calc(x, y) >= 99 :
        print(-1)
        
    else :
        res = 0
        left = 1
        right = x
        
        while left <= right :
            mid = (left + right) // 2
            tmpx = x + mid
            tmpy = y + mid
            
            if calc(tmpx, tmpy) > std :
                res = mid
                right = mid - 1
            else :
                left = mid + 1
        print(res)
                  
game()