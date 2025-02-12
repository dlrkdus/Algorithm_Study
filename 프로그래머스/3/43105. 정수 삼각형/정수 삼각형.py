def solution(triangle):
    answer = 0
    dp = [[0] * len(row) for row in triangle] 
    dp[0][0] = triangle[0][0]
    for i in range(1,len(triangle)):
        for j in range(i+1):
            if i>j>0:
                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            if j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
    
    max_num = -1
    for row in dp:
        max_num = max(max(row),max_num)
    return max_num