a, b, c, x, y = map(int, input().split())

def chicken(a, b, c, x, y) :
    fried = b   #후라이드 2000
    seasoned = a    #양념 1500
    half = c    #반반 0.5 0.5
    seasoned_num = x
    fried_num = y
    minimum = min(x, y)   

    if 2 * c >= a + b :
        price = fried + seasoned
    else :
        price = 2 * half
    
    seasoned_num -= minimum
    fried_num -= minimum

    base = price * minimum
    
    if (2 * half) * (seasoned_num + fried_num) < seasoned_num * seasoned + fried * fried_num :
        plus = (2 * half) * (seasoned_num + fried_num)
    else :
        plus = seasoned_num * seasoned + fried * fried_num
    
    print(base + plus)

chicken(a, b, c, x, y)
