T=int(input())

for test_case in range(1,T+1):
    N, K = map(int,input().split()) #물건 개수, 최대 부피
    dp=[[0]*(K+1) for j in range(N+1)] # 물건 i개 뽑아 j 부피 내 최대 가치
    items = [list(map(int,input().split())) for _ in range(N)] # V = 부피, C = 가치
    for i in range(1,N+1): #물건 몇 개 더할건지지
        for j in range(1,K+1): #부피 몇까지 담을건지
            if items[i-1][0] <= j: #가방 안에 들어가는 부피라면 
                #이전에 더한 값과 현재 더한 값 중 더 큰 값으로 고르자 
                bag_k = j - items[i-1][0] #가방의 남은 용량 = 가방 부피 - 현재 물건 부피
                #가방의 남은 용량에서 뽑을 수 있는 최대 가치에 현재 가치를 더하면 됨
                dp[i][j] = max(dp[i-1][j], dp[i-1][bag_k]+items[i-1][1])
            else: #안 들어간다면 이전 값과 동일
                dp[i][j] = dp[i-1][j]
    print(f"#{test_case}",dp[N][K])