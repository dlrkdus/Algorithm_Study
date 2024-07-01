from collections import deque
N, M, V = map(int,input().split())
graph = [[0 for i in range(N+1)]for j in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a][b]=1

visited = [0 for i in range(N+1)]
visited[V]=1
d=deque()
d.append(V)

def dfs(v):
    print(v,end=" ")
    for i in range(1,N+1):
        if graph[v][i] or graph[i][v]:
            if not visited[i]:
                visited[i]=1
                dfs(i)

def bfs():
    while d:
        x = d.popleft()
        print(x,end=" ")
        for i in range(1,N+1):
            if graph[x][i] or graph[i][x]:
                if not visited[i]:      
                    visited[i]=1
                    d.append(i) 

dfs(V)
print()
visited = [0 for i in range(N+1)]
visited[V]=1
bfs()