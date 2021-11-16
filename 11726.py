def tile() :
    num = int(input())
    
    dp = [0 for _ in range(1001)]
    dp[1] = 1
    dp[2] = 2
    
    if num <= 2 :
        print(dp[num])
    else :
        for i in range(3, num+1) :
            dp[i] = dp[i-2] + dp[i-1]
    
        print(dp[num] % 10007)
    
tile()