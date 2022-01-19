import sys

def serial() :
    n = int(input())
    arr = [sys.stdin.readline().rstrip() for _ in range(n)]
    
    for i in range(len(arr)) :
        sum = 0
        for j in range(len(arr[i])) :
            if ord(arr[i][j]) in range(48, 58) :
                sum += int(arr[i][j])
        arr[i] = [arr[i], sum]
    
    arr.sort(key = lambda x : (len(x[0]), x[1], x))
    
    for a in arr :
        print(a[0])
        
serial()