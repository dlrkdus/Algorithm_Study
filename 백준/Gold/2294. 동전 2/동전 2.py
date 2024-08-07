n, k = map(int,input().split())
coin = []
dp = [10001]*(k+1)
dp[0]=0
for _ in range(n):
    a = int(input())
    if a<=k:
        coin.append(a)
        dp[a]=1

for c in coin:
    for i in range(c,k+1):
        dp[i] = min(dp[i-c]+1,dp[i])

if dp[k]==10001:
    print("-1")
else:
    print(dp[k])