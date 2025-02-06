N, M = map(int,input().split())
money = []
for _ in range(N):
    money.append(int(input()))
money.sort(reverse=True) # 내림차순

dp = [10001] * (1000001)
for i in money:
    dp[i] = 1
for i in range(M+1):
    for m in money:
        dp[i+m] = min(dp[i+m],dp[i] + 1)
if dp[M] == 10001:
    print(-1)
else:
    print(dp[M])