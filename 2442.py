def star() :
    n = int(input())
    
    for i in range(n) :
        print(" " * ((n-1)-i), end = '')
        print("*" * i, end = '')
        
        print("*", end = '')
        
        print("*" * i, end = '')
        print()
        
star()