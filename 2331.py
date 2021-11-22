def repeat() :
        dp = []
        a, p = map(int, input().split())
        dp.append(a)
        
        while 1 :
            sum = 0
            for i in range(len(str(dp[-1]))) :
                sum += int(str(dp[-1])[i]) ** p 

            if sum in dp :
                idx = dp.index(sum)
                print(len(dp) - len(dp[idx:]))
                break
            else :
                dp.append(sum)

repeat()