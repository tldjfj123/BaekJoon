def solution() :
    while 1 :
        arr = list(map(int, input().split()))
        arr.sort()
        
        if sum(arr) == 0 :
            break
        
        if arr[2] >= arr[1] + arr[0] :
            print('Invalid')
        else : 
            if len(set(arr)) == 3 :
                print('Scalene')
            elif len(set(arr)) == 2 :
                print('Isosceles')
            else :
                print('Equilateral')

solution()