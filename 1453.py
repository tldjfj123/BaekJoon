def pc() :
    n = int(input())
    seat = [0 for _ in range(100)]
    customer = list(map(int, input().split()))
    
    false = 0
    for c in customer :
        if seat[c-1] == 0 :
            seat[c-1] = 1
        else :
            false += 1
    
    print(false)
    
pc()