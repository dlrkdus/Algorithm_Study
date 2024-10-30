def solution(triangle):
    answer = 0
    dp = [[0] * len(row) for row in triangle]  # 각 행마다 리스트 생성
    dp[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:  # 맨 왼쪽 열일 경우
                dp[i][j] = dp[i-1][j] + triangle[i][j] #위 행의 같은 열에게만 받을 수 있음
            elif j == len(triangle[i]) - 1:  # 맨 오른쪽 열일 경우
                dp[i][j] = dp[i-1][j-1] + triangle[i][j] #위 행의 -1열에서만 받을 수 있음
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

    
    return max(dp[len(triangle)-1])