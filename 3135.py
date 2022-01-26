def radio() :
    a, b = map(int, input().split()) # target : b
    n = int(input())
    board = [int(input()) for _ in range(n)]
    
    res = []
    for i in board :
        res.append(abs(b - i)+1)
    res.append(abs(b-a))
    
    print(min(res))
        
radio()