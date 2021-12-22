def rev() :
    x, y = input().split()
    
    x, y = int(x[::-1]), int(y[::-1])
    
    print(int(str(x + y)[::-1]))
    
rev()