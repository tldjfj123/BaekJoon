def center() :
    n = int(input())
    
    dots = []
    
    for i in range(n) :
        if i == 0 :
            dots.append(3)
        else :
            dots.append(dots[-1] + 2 ** i)
    
    print(dots[-1] ** 2)

center()