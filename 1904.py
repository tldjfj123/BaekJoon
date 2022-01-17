def tile() :
    n = int(input())
    
    if n <= 2 :
        if n == 1 :
            return 1
        else :
            return 2
    else :
        dp = [0 for _ in range(n)]
        dp[0] = 1
        dp[1] = 2
        
        for i in range(2, n) :
            dp[i] = (dp[i-1] + dp[i-2]) % 15746
        
        return dp[-1]

print(tile())