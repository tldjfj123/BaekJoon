import sys

num = int(sys.stdin.readline())

def arrow(n) :
    arr = list(map(int, sys.stdin.readline().split()))
    res = []
    for i in range(n-1) :
        count = 0
        for j in range(i+1, n) :
            if arr[i] > arr[j] :
                count += 1
            else :
                break
        res.append(count)
    print(max(res))                
    
arrow(num)