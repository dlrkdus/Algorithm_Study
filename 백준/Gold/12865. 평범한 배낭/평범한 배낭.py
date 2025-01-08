N, K = map(int,input().split())
# N = 물건 갯수 K = 최대 무게
dp = [0]*(K+1) # 무게 당 최대 가치
weights = []
values = []

for _ in range(N):
    w, v = map(int,input().split())
    weights.append(w)
    values.append(v)

for i in range(N): # 갯수
    for j in range(K,0,-1): # 무게
        if weights[i] <= j: # j = 현재 가방에 남은 무게
            dp[j] = max(dp[j],dp[j-weights[i]]+values[i])

print(dp[K])

