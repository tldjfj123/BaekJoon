x = int(input())
y = int(input())

def Quadrant(x, y) :
    if x > 0 and y > 0 :
        return 1
    elif x < 0 and y > 0 :
        return 2
    elif x < 0 and y < 0 : 
        return 3
    else :
        return 4

print(Quadrant(x, y))
