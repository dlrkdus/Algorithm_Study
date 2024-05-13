T=int(input())

def dfs(x,y,count):
    global max_count
    visited[x][y]=1
    if arr[x][y]==0:
        return 
    max_count = max(count,max_count)

    nx = [0,0,1,-1]
    ny = [1,-1,0,0]
    for i in range(4):
        new_x = x+nx[i]
        new_y = y+ny[i]
        if 0<=new_x<M and 0<=new_y<N and visited[new_x][new_y]==0:
            dfs(new_x,new_y,count+1)
    visited[x][y]=0


for test_case in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for i in range(M)]for j in range(N)]

    # max_count = 0

    # for i in range(M):
    #     for j in range(N):
    #         if arr[i][j]==1 and visited[i][j]==0:
    #             dfs(i,j,1)
    answer =[]
    for i in range(N):
        count=0
        for j in range(M):
            if arr[i][j]==1:
                count+=1
            if j ==M-1 or arr[i][j]==0:
                answer.append(count)
                count=0

    for i in range(M):
        count=0
        for j in range(N):
            if arr[j][i]==1:
                count+=1
            if j ==N-1 or arr[j][i]==0:
                answer.append(count)
                count=0


    # print(f"#{test_case}",max_count)
    print(f"#{test_case}",max(answer))

