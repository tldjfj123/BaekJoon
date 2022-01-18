def ranking() :
    n, score, p = map(int, input().split())
    if n == 0 :
        return 1
    
    scoreboard = list(map(int, input().split()))
    
    if n == p and score <= scoreboard[-1] :
        return -1
    else :
        for i in range(len(scoreboard)) :
            if score >= scoreboard[i] :
                return i+1
        else :
            return n + 1

print(ranking())