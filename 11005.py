def solution() :
    a, b = map(int, input().split())
    std = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = []
    while a != 0 :
        res.append(str(std[a % b]))
        a //= b
    
    print(''.join(res)[::-1])
        
solution()