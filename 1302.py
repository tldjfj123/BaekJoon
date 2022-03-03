def solution() :
    n = int(input())
    sold = dict()
    
    for _ in range(n) :
        title = input()
        
        if title not in sold.keys() :
            sold[title] = 1
        else :
            sold[title] += 1
    
    print(sorted(list(sold.items()), key = lambda x : (-x[1], x[0]))[0][0])

solution()