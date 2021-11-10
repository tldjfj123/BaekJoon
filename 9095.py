def plus() :
    num = int(input())
    
    for _ in range(num) :
        n = int(input())
        dp = [0 for _ in range(12)]
        
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        
        if n == 1 :
            print(dp[1])
        elif n == 2 :
            print(dp[2])
        elif n == 3 :
            print(dp[3])
        else :
            for i in range(4, 12) :
                dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
            print(dp[n])
        
plus()
