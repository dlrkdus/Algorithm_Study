import copy
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
# dp에 이전 방향을 저장해놔야 한다.
# dp[i][j][0] = 왼쪽에서 옴 [1] = 위에서 옴 [2] = 오른쪽에서 옴
dp = [[[float('inf')]*3 for _ in range(m)] for i in range(n)]
for j in range(m):
    dp[0][j] = [arr[0][j]]*3

for i in range(1, n):
    for j in range(m):
        # 오른쪽으로 내려갈 경우
        if j!=m-1:
            dp[i][j][2] = arr[i][j] + min(dp[i-1][j+1][0], dp[i-1][j+1][1])
        # 왼쪽으로 내려갈 경우
        if j != 0:
            dp[i][j][0] = arr[i][j] + min(dp[i-1][j-1][1], dp[i-1][j-1][2])
        # 아래로 내려갈 경우
        dp[i][j][1] = arr[i][j] + min(dp[i-1][j][0], dp[i-1][j][2])

answer = 100000000
for i in range(m):
    answer = min(answer,min(dp[n-1][i]))
print(answer)

        

