def padovan() :
    n = int(input())
    
    for _ in range(n) :
        num = int(input())    
        dp = [0 for _ in range(100)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 1
        if num <= 2 :
            print(dp[num])
        else :
            for i in range(3, num) :
                dp[i] = dp[i-2] + dp[i-3]
            print(dp[num-1])             

padovan()