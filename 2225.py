"""
1 2 3 4 5 6
1 3 6 10 15 21
1 4 10 20 35 56
1 5 15 35 70 126
1 6 21 56 126 252
1 7 28 84 210 462
"""
from itertools import product

def pd() :
    n, k = map(int, input().split())
    
    arr = [[i for i in range(1, k+1)]]
    
    for _ in range(n-1) :
        arr.append([1 for _ in range(k)])
    
    for i in range(1, n) :  #row
        for j in range(1, len(arr[i])) :   #column
            arr[i][j] = (arr[i-1][j] + arr[i][j-1]) % 1000000000 
    
    print(arr[n-1][k-1])  
      
pd()