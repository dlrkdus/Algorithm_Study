N = int(input()) #컴퓨터 개수 
M = int(input()) #컴퓨터 연결 쌍
computer = [[0 for i in range(N+1)]for j in range(N+1)]
visited = [0 for i in range(N+1)]
cnt = 0
for i in range(M):
    a,b = map(int,input().split())
    computer[a][b]=1
    computer[b][a]=1

def dfs(v):
    global cnt
    visited[v]=1
    for i in range(N+1):
        if computer[v][i] or computer[i][v]:
            if not visited[i]:
                cnt+=1
                dfs(i)

dfs(1)
print(cnt)


