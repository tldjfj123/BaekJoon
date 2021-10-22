"""
도착 계단(n)의 관점에서 생각해보면
1) n-2
2) n-1
두개의 경우에서 시작됐다고 생각할 수 있다.

1)의 경우는 전전계단이 상관이 없다.
2)의 경우는 조건에 연속 3번 1씩 이동은 안된다 하였기 때문에 반드시 n-3에서 출발했어야만 한다.

이에대한 점화식을 세워보면

1) dp[i-2] + s[i]
2) dp[i-3] + s[i-1] + s[i]

* dp[i] : i번째 계단까지 오르는데의 최댓값
"""


def stair() :
    n = int(input())
    s = [0 for _ in range(301)]

    for i in range(n) :
        s[i] = int(input())
    
    dp = [0 for _ in range(301)]

    dp[0] = s[0]
    dp[1] = s[0] + s[1]
    dp[2] = max(s[1] + s[2], s[0] + s[2])

    for i in range(3, n) :
        dp[i] = max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i])

    print(dp[n-1])  

stair()