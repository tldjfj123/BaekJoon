a, b = input().split()

def s(x, y) :
    x = list(x)
    y = list(y)
    x.reverse()
    y.reverse()
    
    new_x = int(''.join(x))
    new_y = int(''.join(y))

    if new_x > new_y :
        return new_x
    return new_y   

print(s(a, b))