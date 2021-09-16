fruit, length = map(int, input().split())
height = list(map(int, input().split()))

def sneakbird(f, l, h) :
    height.sort()
    for x in height :
        if x <= l :
            l += 1
        else :
            pass

    return l 

print(sneakbird(fruit, length, height))
