import sys

def keep() :
    n = sys.stdin.readline().rstrip()
    count = 0 
    dp = [0 for _ in range(len(n)+1)]
    
    if len(n) == 1 :
        print(int(n))
    else :
        for i in range(1, len(n)) :
            dp[i] = 9 * (10 ** (i-1)) * i
        
        dp[len(n)] = ((int(n) - (10 ** (len(n)-1))) + 1) * len(n)
        
        print(sum(dp))
    
keep()