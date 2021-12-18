def star() :
    n = int(input())
    
    for i in range(n) :
        print(" " * i, end = '')
        print("*" * (n-1-i), end = '')

        print("*", end = '')

        print("*" * (n-1-i), end = '')
        
        print()
    
    for i in range(1, n) :
        print(" " * (n-1-i), end = '')
        print("*" * i, end = '')
    
        print("*", end = '')

        print("*" * i, end = '')
        
        print()
    
star()