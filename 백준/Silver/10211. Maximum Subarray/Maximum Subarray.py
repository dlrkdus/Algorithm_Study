T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    dp = [0] * N # i번째 요소까지 더했을 때 최대 부분합 저장
    dp[0] = arr[0]
    for i in range(1,N):
        dp[i] = max(dp[i-1] + arr[i], arr[i]) # 이전 부분합을 합하는게 큰지, 버리는게 큰지
    print(max(dp))