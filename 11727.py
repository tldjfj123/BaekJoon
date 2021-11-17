def tile() :
    num = int(input())
    
    if num == 1 :
        dp = [1]
        print(dp[-1])
    elif num == 2 :
        dp = [1, 3]
        print(dp[-1])
    else :
        dp = [0 for _ in range(num+1)]
        dp[1] =  1
        dp[2] = 3
        
        for i in range(3, num+1) :
            if i % 2 == 1 :
                dp[i] = 2 * dp[i-2] + dp[i-1]
            else :
                dp[i] = 2 * dp[i-1] + 1
        print(dp[-1] % 10007)
tile()