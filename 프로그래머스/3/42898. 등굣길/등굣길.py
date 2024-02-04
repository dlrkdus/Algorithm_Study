def solution(m, n, puddles):
    MOD = 1000000007
    dp = [[0] * (m + 1) for _ in range(n + 1)]  

    # 웅덩이가 있는 위치는 -1로 초기화
    for puddle in puddles:
        dp[puddle[1]][puddle[0]] = -1

    # 시작 지점은 1로 초기화
    dp[1][1] = 1

    # dp[i][j] = dp[i-1][j] + dp[i][j-1] (웅덩이가 아닌 경우)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1:  # 웅덩이가 있는 경우
                dp[i][j] = 0
            else:
                # 왼쪽과 위쪽의 최단 경로 수를 더함
                if dp[i-1][j] != -1:
                    dp[i][j] += dp[i-1][j]
                if dp[i][j-1] != -1:
                    dp[i][j] += dp[i][j-1]
                dp[i][j] %= MOD

    return dp[n][m]