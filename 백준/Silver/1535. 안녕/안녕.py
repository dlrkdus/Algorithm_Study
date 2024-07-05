N = int(input())
weight = list(map(int,input().split())) #무게
value = list(map(int,input().split())) #기쁨
dp = [0]*100 # 키로(손해)당 최대 기쁨 

# 각 사람에게 한 번만 인사할 수 있으므로 제로원 냅색이다. 

for i in range(N):
    for j in range(99,0,-1):
        if weight[i]<=j:
            dp[j]=max(dp[j],dp[j-weight[i]]+value[i])

print(dp[99])

