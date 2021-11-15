import sys

def section() :
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    sum_list = [0]
    total = 0
    
    for i in range(len(arr)) :
        total += arr[i]
        sum_list.append(total) 
    
    for _ in range(m) :
        i, j = map(int, sys.stdin.readline().split())
        print(sum_list[j] - sum_list[i-1])
            
section()