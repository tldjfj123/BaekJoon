import sys

def memory() :
    t = int(sys.stdin.readline())
    
    for _ in range(t) :
        n = int(sys.stdin.readline())
        na = list(map(int, sys.stdin.readline().split()))
        m = int(sys.stdin.readline()) 
        ma = list(map(int, sys.stdin.readline().split()))
        
        na.sort()
        
        for factor in ma :
            left = 0
            right = n-1
            
            while left <= right :
                mid = (left + right) // 2
                
                if na[mid] == factor :
                    print(1)
                    break
                elif na[mid] > factor :
                    right = mid - 1
                else :
                    left = mid + 1
            else :
                print(0)

memory()