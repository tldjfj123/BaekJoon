case = int(input())

def president(n) :
    for i in range(n) :
        k = int(input())+1    # 층
        n = int(input())    # 호
        arr = []
        arr.append([i for i in range(1, n+1)])
        for i in range(k-1) :
            arr.append([0 for i in range(n)])
        for x in range(1, k) :
            for y in range(n) :
                arr[x][y] += (sum(arr[x-1][:y]) + arr[x-1][y])
        print(arr[k-1][n-1])
            
president(case)