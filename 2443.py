def star() :
    n = int(input())
    
    for i in range(n) :
        print(" " * i, end = '')
        print("*" * ((n-1)-i), end = '')
        
        print("*", end = '')

        print("*" * ((n-1)-i), end = '')
        print()
        
star()