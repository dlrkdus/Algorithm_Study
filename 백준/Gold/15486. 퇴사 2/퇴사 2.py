N = int(input())
T = []
P = []
for _ in range(N):
    t, p = map(int,input().split())
    T.append(t)
    P.append(p)
dp = [0] * (N+2) # dp[i] = i일 이후로 벌 수 있는 최대 금액
# 당일 상담을 했을 때와 안 했을 때 max

for i in range(N,0,-1):
    # 상담을 안 했을 때를 기본으로 
    dp[i] = dp[i+1]
    # 상담이 가능할 경우
    if i+T[i-1] <=N+1:
        dp[i] = max(dp[i],P[i-1]+dp[i+T[i-1]])
print(max(dp))
