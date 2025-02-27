# 모든 경로 문제니까 DFS다.
import sys
sys.setrecursionlimit(10 ** 9)
M, N = map(int,input().split())
arr = [list(map(int,input().split()))for _ in range(M)]
v = [[-1 for i in range(N)]for j in range(M)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x, y):
    if x == M-1 and y == N-1:
        return 1
    if v[x][y] == -1: # 방문하지 않은 곳이라면 
        v[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<M and 0<=ny<N:
                if arr[nx][ny] < arr[x][y]:
                    v[x][y] += dfs(nx, ny)
    # 백트래킹을 위한 리턴
    return v[x][y]

print(dfs(0,0))