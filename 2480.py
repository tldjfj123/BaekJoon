def solution() :
    a = list(map(int, input().split()))
    arr = list(set(a))
    
    if len(arr) == 3 :
        print(max(arr) * 100)
    elif len(arr) == 1 :
        print(10000 + arr[0] * 1000)
    else :
        print(1000 + (sum(a) - sum(arr)) * 100)
    
solution()