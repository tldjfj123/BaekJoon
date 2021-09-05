h, m = input().split()

h = int(h)
m = int(m)

def alarm(h, m) :
    if m < 45 and h > 0 :
        h -= 1
        m += 15
        print(h, m)
    elif m < 45 and h == 0 :
        h += 23
        m += 15
        print(h, m)
    else :
        m -= 45
        print(h, m)

alarm(h, m)