N, K = map(int,input().split())
weight = []
value = []
dp = [0] *(K+1)
for _ in range(N):
    W, V = map(int,input().split())
    weight.append(W)
    value.append(V)

for i in range(N):
    for j in range(K,0,-1):
        if weight[i]<=j:
            dp[j] = max(dp[j],dp[j-weight[i]]+value[i])

print(dp[K])


