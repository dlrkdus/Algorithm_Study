N = int(input())
counsel = []
for _ in range(N):
    counsel.append(list(map(int,input().split())))
dp = [0] * (N*2)
for i in range(N):
    if counsel[i][0] <= N-i:
        dp[i] = counsel[i][1]

for i in range(N-1,-1,-1):
    if counsel[i][0]<=N-i:
        max_sum = 0
        for j in range(i+counsel[i][0],N):
            max_sum = max(max_sum,dp[j])
        dp[i] = counsel[i][1] + max_sum
print(max(dp))
