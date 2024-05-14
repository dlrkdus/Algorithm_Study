T=int(input())
for test_case in range(1,T+1):
    N = int(input())
    snail = [[0 for i in range(N)] for j in range(N)]
    cnt = 0
    num = 1
    while(num <N*N):
        for i in range(cnt,N-cnt-1): # 우
            snail[cnt][i] = num
            num+=1
        for i in range(cnt,N-cnt-1): #하 1,3 2,3 3,3
            snail[i][N-cnt-1] = num
            num+=1
        for i in range(N-cnt-1,cnt,-1): #좌 3,2 3,1 3,0 
            snail[N-cnt-1][i] = num
            num+=1
        for i in range(N-cnt-1,cnt,-1): # 상 3,0 2,0 1,0
            snail[i][cnt] = num
            num+=1
        cnt+=1
    if N%2!=0:
        snail[(N-1)//2][(N-1)//2] = num
            
    print(f"#{test_case}")
    for i in snail:
        for j in i:
            print(j, end=" ")
        print()
        

