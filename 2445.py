def star() :
    n = int(input())
    
    for i in range(1, n) :
        print("*" * i, end = '')
        print(" " * (n-i), end = '')
        print(" " * (n-i), end = '')
        print("*" * i, end = '')
        print()
        
    print("*" * (2*n))
    
    for i in range(1, n) :
        print("*" * (n-i), end = '')
        print(" " * i, end = '')
        print(" " * i, end = '')
        print("*" * (n-i), end = '')
        print()
        
star()