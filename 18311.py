def solution() :
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    res = [i for i in enumerate(arr, start = 1)]
    res = res + res[::-1]
    
    sum = 0
    for i in range(len(res)) :
        sum += res[i][1]
        if sum == k :
            print(res[i+1][0])
            break
        elif sum > k :
            print(res[i][0])
            break
        
solution()