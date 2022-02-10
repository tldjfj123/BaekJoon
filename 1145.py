def solution() :
    arr = list(map(int, input().split()))
    
    count = 0
    num = 1
    while 1 :    
        for i in range(len(arr)) :
            if num % arr[i] == 0 :
                count += 1
            if count == 3 :
                return num
        else :
            num += 1
            count = 0
                
print(solution())