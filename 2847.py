def game() :
    n = int(input())
    arr = []
    for _ in range(n) :
        arr.append(int(input()))
    
    arr = arr[::-1]
    
    count = 0
    
    for i in range(1, len(arr)) :
        if arr[i-1] <= arr[i] :
            std = arr[i-1]-1
            count += arr[i] - std
            arr[i] = std
    print(count)
               
game()