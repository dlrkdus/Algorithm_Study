N = int(input())
counsel = []
for _ in range(N):
    counsel.append(list(map(int,input().split())))
dp = [0] * (N*2)

for i in range(N):
    # 현재 상담을 진행하지 않고 다음날로 넘어간다면
    dp[i+1] = max(dp[i+1],dp[i])
    # 상담이 가능해서 진행한다면
    if i + counsel[i][0] <= N:
        dp[i+counsel[i][0]] = max(dp[i+counsel[i][0]], dp[i] + counsel[i][1])

print(max(dp))