import sys

def mul() :
    n = int(sys.stdin.readline())
    dp = [0 for _ in range(n)]
    arr = [float(sys.stdin.readline()) for _ in range(n)]

    for i in range(len(arr)) :
        dp[i] = arr[i]
        for j in range(i+1, len(arr)) :
            arr[i] *= arr[j]
            dp[i] = max(arr[i], dp[i])
    print("{:.3f}".format(max(dp)))

mul()