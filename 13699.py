def ignite() :
    n = int(input())
    dp = [0 for _ in range(n+1)]
    dp[0] = 1

    for i in range(1, n+1) :
        for j in range(0, i) :
            dp[i] += dp[j] * dp[i-j-1]
    print(dp[-1])       

ignite()