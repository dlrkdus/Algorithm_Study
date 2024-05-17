T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    dp = [1 for i in range(N)]

    # 1 3 2 5 4 
    # dp[1] = 1
    # dp[2] = 2
    # dp[3] = 2
    # dp[4] = 3
    # dp[5] = 3

    for i in range(N):
        for j in range(i):
            if arr[i]>arr[j]:
                dp[i] = max(dp[i],dp[j]+1)
    print(f"#{test_case}",max(dp))