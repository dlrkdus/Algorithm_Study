import sys
sys.setrecursionlimit(10 ** 6)
N, M, K = map(int,input().split())
arr = [[0 for i in range(M)]for j in range(N)]
visited = [[0 for i in range(M)]for j in range(N)]
for _ in range(K):
    r, c = map(int,input().split())
    arr[r-1][c-1]=1
maxFood = 0
nx = [0,0,1,-1]
ny = [1,-1,0,0]

def dfs(i,j):
    global count
    for x in range(4):
        new_x = i + nx[x]
        new_y = j + ny[x]
        if 0<=new_x<N and 0<=new_y<M and arr[new_x][new_y]==1 and not visited[new_x][new_y]:
            visited[new_x][new_y]=1
            count+=1
            dfs(new_x,new_y)


for i in range(N):
    for j in range(M):
        if arr[i][j]==1 and not visited[i][j]:
            count = 0
            dfs(i,j)
            maxFood = max(maxFood,count)

print(maxFood)